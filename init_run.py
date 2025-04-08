import os

from dotenv import load_dotenv

from src.docker_utils import (
    build_docker_image,
    is_container_running,
    is_image_built,
    run_docker_image,
)
from src.huggingface_download import save


def model_download():
    os.makedirs("model_build", exist_ok=True)

    print("Model not found. Downloading...")

    api_key = os.getenv("HUGGINGFACE_API_KEY", None)
    repo_id = "google/gemma-3-4b-it"

    save(api_key=api_key, repo_id=repo_id)
    print("Model downloaded.")


def main() -> None:
    load_dotenv()

    tag = "gemma3-4b-vllm-api-server"
    container_name = tag

    # 1. Model Download
    if not os.path.exists("model_build/gemma-3-4b-it"):
        print("model downloading...")
        model_download()

    # 2. Docker Build
    if not is_image_built(tag=tag):
        print("Docker image building...")
        build_docker_image(dockerfile_path="dockerfile", tag=tag)

    # 3. Docker Run
    if not is_container_running(container_name=container_name):
        print("Docker running...")
        run_docker_image(tag=tag, container_name=container_name)


if __name__ == "__main__":
    main()
