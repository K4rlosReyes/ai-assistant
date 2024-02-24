from typing import Any

# Importing functions from other modules
from core.process.vector_store import get_query_engine, load_db, load_data


def ask_model(query: str, index: Any) -> Any:
    """
    Query the model with a given input.

    Args:
        query (str): The input query.
        index (Any): The index used for querying.

    Returns:
        Any: The response from the model.
    """
    query_engine = get_query_engine(index)
    response = query_engine.query(query)
    return response


if __name__ == "__main__":
    # Set the path to the data
    path = "tmp_uploads/"
    # Load the vector store
    vector_store = load_db()
    # Load data and create an index
    index = load_data(vector_store=vector_store, path=path)

    while True:
        # Prompt user for input
        query = input("Ask something (or type 'exit'): ")

        # Exit the loop if the user types 'exit'
        if query.lower() == "exit":
            break

        # Get the model's response
        answer = ask_model(query=query, index=index)
        print(answer)
