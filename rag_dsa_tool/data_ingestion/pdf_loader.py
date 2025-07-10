from langchain_community.document_loaders import PyPDFDirectoryLoader


DATA_PATH = "rag_dsa_app/data_ingestion/data"

def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()

