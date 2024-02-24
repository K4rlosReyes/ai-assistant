import os
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)
from llama_index.llms.openai import OpenAI
from core.manager import settings
import requests

MODEL = "llama"

# LLM selection
if MODEL == "openai":
    print("USE OPENAI")
    # Use OpenAI model
    llm = OpenAI(api_key=settings.OPENAI_KEY)

else:  # Default to Llama
    print("USE LLAMA")
    model_url: str = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q4_0.gguf"
    # model_path: str = "core/models/llama-2-13b-chat.Q2_K.gguf"

    # TODO: Save the model automatically the first time
    # Check if model is already downloaded
    # if not os.path.exists(model_path):
    #     print("Model not found. Downloading...")
    #     response = requests.get(model_url)
    #     with open(model_path, "wb") as f:
    #         f.write(response.content)
    #     print("Model downloaded and saved.")
    # else:
    #     print("Model found.")

    llm = LlamaCPP(
        model_url=model_url,
        # model_path=model_path,
        temperature=0.1,
        max_new_tokens=256,
        context_window=3900,
        model_kwargs={"n_gpu_layers": 0},  # set GPU layers to 1 if you have one
        verbose=True,
        messages_to_prompt=messages_to_prompt,  # providing additional parameters
        completion_to_prompt=completion_to_prompt,  # providing additional parameters
    )
if __name__ == "__main__":
    print("LLM")
