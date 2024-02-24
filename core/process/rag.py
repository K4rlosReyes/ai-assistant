from typing import Any

# Importing functions from other modules
from core.process.vector_store import get_query_engine, load_db, load_data


def ask_model(query: str, index: Any) -> str:
    """
    Query the model with a given input.

    Args:
        query (str): The input query.
        index (Any): The index used for querying.

    Returns:
        str: The response from the model.
    """
    query_engine = get_query_engine(index)
    response = query_engine.query(query)
    return response


# TODO: Optimize the findings of documents
# (eg. search documents at the beggining and then only if new documents are added)
def run_rag(query: str) -> str:
    """
    Run the retrieval augmented generation (RAG) model to answer a given query.

    Args:
        query (str): The query to be answered.

    Returns:
        str: The generated answer.
    """
    # Set the path to the data
    path: str = "tmp_uploads/"
    # Load the vector store
    vector_store: Any = load_db()
    # Load data and create an index
    index: Any = load_data(vector_store=vector_store, path=path)
    # Retrieving answer
    answer: str = ask_model(query=query, index=index)
    return answer


if __name__ == "__main__":
    # Set the path to the data
    path: str = "tmp_uploads/"
    # Load the vector store
    vector_store: Any = load_db()
    # Load data and create an index
    index: Any = load_data(vector_store=vector_store, path=path)

    while True:
        # Prompt user for input
        query: str = input("Ask something (or type 'exit'): ")

        # Exit the loop if the user types 'exit'
        if query.lower() == "exit":
            break

        # Get the model's response
        answer: str = ask_model(query=query, index=index)
        print(answer)
