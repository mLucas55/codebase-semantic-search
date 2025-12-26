from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='codevec',
    version='1.0.0',
    author="Lucas Monroe",
    author_email="lucas.i.monroe1@gmail.com",
    description="Semantic search for Python codebases using embeddings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mlucas55/codevec",
    packages=find_packages(),
    install_requires=[
        'chromadb',
        'sentence-transformers',
        'fastapi',
        'uvicorn',
        'requests',
    ],
    entry_points={
        "console_scripts": [
            "vec = codevec:show_help",
            "vec-index = codevec:indexer",
            "vec-search = codevec:searcher",
            "vec-server = codevec.server:run_server",
        ]
    }
)