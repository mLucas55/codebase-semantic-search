from google import genai
from google.genai import types
import chromadb
import sys

from dotenv import load_dotenv
import os

load_dotenv()
GEMENI_KEY = os.getenv("GEMENI_KEY")

gemeni = genai.Client(api_key=GEMENI_KEY)

# Load ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

try:
    collection = client.get_collection("code_index")
except Exception as e:
    print(f"❌ Error: Could not load index. Have you run index.py first?")
    print(f"   Details: {e}")
    sys.exit(1)

def generate_query_embedding(query):
    """Generate embedding for the search query"""
    response = gemeni.models.embed_content(
        model="gemini-embedding-001",
        contents=query,
        config=types.EmbedContentConfig(task_type="CODE_RETRIEVAL_QUERY")
    )
    
    # Extract the values from the first embedding
    return response.embeddings[0].values

def search_code(query, n_results=5):
    """Search the indexed codebase"""
    print(f"🔍 Searching for: '{query}'")
    print("🔮 Generating query embedding...\n")
    
    # Generate query embedding
    query_embedding = generate_query_embedding(query)
    
    # Search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    
    if not results['documents'][0]:
        print("❌ No results found")
        return
    
    print(f"✨ Found {len(results['documents'][0])} results:\n")
    print("=" * 80)
    
    # Display results
    for i, (doc, metadata, distance) in enumerate(zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0]
    ), 1):
        
        similarity = 1 - distance  # Convert distance to similarity score
        
        print(f"\n🎯 Result #{i} (similarity: {similarity:.2%})")
        print(f"📁 File: {metadata['file_path']}:{metadata['line']}")
        print(f"🏷️  Function: {metadata['name']}")
        
        print(f"\n📝 Code:")
        print("─" * 80)
        # Show the code with some formatting
        code_lines = doc.split('\n')
        for line in code_lines[:20]:  # Show first 20 lines
            print(f"   {line}")
        if len(code_lines) > 20:
            print("   ...")
        print("─" * 80)
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search.py <query>")
        print('Example: python search.py "find email validation"')
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])  # Join all args in case query has spaces
    search_code(query)