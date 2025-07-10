from rag_dsa_tool.data_ingestion.pdf_loader import load_documents
from rag_dsa_tool.preprocessing.chunking import split_documents
from rag_dsa_tool.vector_store.chroma_db import add_to_chroma, clear_database

import argparse

def main():
    # Check if the database should be cleared (using the --clear flag).
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("Clearing Database")
        clear_database()

    # Create (or update) the data store.
    documents = load_documents()
    chunks = split_documents(documents)
    add_to_chroma(chunks)

if __name__ == "__main__":
    main() 

