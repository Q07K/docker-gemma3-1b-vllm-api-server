import os

from dotenv import load_dotenv

from src.local_api import generate


def main(query: str):
    load_dotenv()

    # Local API Call
    base_url = "http://localhost:8000/v1"
    api_key = os.getenv("LOCAL_MODEL_API_KEY", None)
    generate(
        base_url=base_url,
        api_key=api_key,
        model="gemma-3-4b-it",
        query=query,
    )


if __name__ == "__main__":
    main(query="안녕하세요?")
