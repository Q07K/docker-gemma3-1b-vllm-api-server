import os

from dotenv import load_dotenv

from src.huggingface_download import save


def main() -> None:
    load_dotenv()
    repo_id = "google/gemma-3-1b-it"
    api_key = os.getenv("HUGGINGFACE_API_KEY", None)

    if not os.path.exists(repo_id):
        save(api_key=api_key, repo_id=repo_id)


if __name__ == "__main__":
    main()
