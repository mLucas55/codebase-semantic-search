from google import genai

from dotenv import load_dotenv
import os

load_dotenv()

GEMENI_KEY = os.getenv("GEMENI_KEY")

client = genai.Client(api_key=GEMENI_KEY)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Tell me about typesrcipt in a few words",
)

print(response.text)