from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding
from core.manager import settings

embedding = "openai"

if embedding == "openai":
    embed_model = OpenAIEmbedding(
        model="text-embedding-3-large", api_key=settings.OPENAI_KEY, dimensions=384
    )

else:
    # Initialize the HuggingFaceEmbedding instance with the desired model
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

if __name__ == "__main__":
    print("EMBEDDINGS")
