import os

from dotenv import load_dotenv
from openai import OpenAI


def main(query: str):
    load_dotenv()

    base_url = "http://localhost:8000/v1"
    api_key = os.getenv("LOCAL_MODEL_API_KEY", None)
    api_key = "$LOCAL_MODEL_API_KEY"

    client = OpenAI(
        base_url=base_url,
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        model="google/gemma-3-1b-it",
        messages=[
            {"role": "user", "content": query},
        ],
        temperature=0.4,
        stream=True,
    )

    for token in completion:
        print(token.choices[0].delta.content, end="", flush=True)


if __name__ == "__main__":
    main(query="안녕")
