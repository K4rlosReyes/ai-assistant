from typing import Any
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
import chromadb

from core.process.embedding import embed_model
from core.process.llm import llm


def load_db() -> ChromaVectorStore:
    """
    Load or create a ChromaVectorStore instance.
    """
    # Load or create ChromaDB
    db = chromadb.PersistentClient(path="core/schemas/chroma_db")
    chroma_collection = db.get_or_create_collection("rag")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    return vector_store


def load_data(path: str, vector_store: ChromaVectorStore) -> VectorStoreIndex:
    """
    Load data from a given path and create a VectorStoreIndex.

    Args:
        path (str): Path to the data.
        vector_store (ChromaVectorStore): ChromaVectorStore instance.

    Returns:
        VectorStoreIndex: Index created from the loaded data.
    """
    # Create a storage context
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    # Load data from the given path
    documents = SimpleDirectoryReader(path).load_data()
    # Create an index from the loaded documents
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model
    )
    return index


def get_query_engine(index: VectorStoreIndex) -> Any:
    """
    Get a query engine for the given index.

    Args:
        index (VectorStoreIndex): Index to create the query engine from.

    Returns:
        Any: Query engine created from the index.
    """
    # Create and return a query engine for the index
    query_engine = index.as_query_engine(llm=llm)
    return query_engine


if __name__ == "__main__":
    # Entry point of the script
    print("VECTOR STORE")
