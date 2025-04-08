"""Docker utils"""

import docker


def is_image_built(tag: str) -> bool:
    """Checks if a Docker image with the given tag exists locally.

    Parameters
    ----------
    tag : str
        Tag to assign to the built Docker image

    Returns
    -------
    bool
        True if the image exists, False otherwise.
    """
    try:
        client = docker.from_env()

        # Try to get the image by tag
        client.images.get(tag)
        return True

    except docker.errors.ImageNotFound:
        return False

    except Exception as e:
        print(f"Error while checking image: {e}")
        return False


def build_docker_image(dockerfile_path: str, tag: str) -> None:
    """Builds a Docker image using the specified Dockerfile.

    Parameters
    ----------
    dockerfile_path : str
        Path to the Dockerfile.
    tag : str
        Tag to assign to the built Docker image
    """
    try:
        client = docker.from_env()
        print("Docker 클라이언트 생성 성공")  # 추가
        generator = client.api.build(
            dockerfile=dockerfile_path,
            tag=tag,
            path="model_build",
            decode=True,
        )
        print("Docker 빌드 시작")  # 추가
        for chunk in generator:
            if "stream" in chunk:
                print(chunk["stream"], end="", flush=True)

        print(f"Docker image Build Success: {tag}")

    except docker.errors.BuildError as e:
        print(f"Docker image build failed: {tag}")
        print(f"Error message: \n{e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def run_docker_image(tag: str, container_name: str) -> None:
    """Runs a Docker container from the specified image tag.

    Parameters
    ----------
    tag : str
        Tag to assign to the built Docker image
    container_name : str, optional
        Name of the container
    """
    try:
        client = docker.from_env()

        # Run the container
        container = client.containers.run(
            image=tag,
            name=container_name,
            detach=True,
            tty=True,
            stdin_open=True,
            ports={"8000/tcp": 8000},
            runtime="nvidia",  # Required for GPU support
            device_requests=[  # Request all available GPUs
                docker.types.DeviceRequest(count=-1, capabilities=[["gpu"]])
            ],
        )

        print(f"Container '{container_name}' is running from image '{tag}'.")
        print(f"Container ID: {container.id}")

    except docker.errors.APIError as e:
        print(f"Failed to run container: {e.explanation}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def start_existing_container(container_name: str) -> None:
    """Starts an existing Docker container by name.

    Parameters
    ----------
    container_name : str
        Name of the container
    """
    try:
        client = docker.from_env()

        # Get the container by name
        container = client.containers.get(container_name)

        # Start the container
        container.start()

        print(f"Container '{container_name}' has been started.")

    except docker.errors.NotFound:
        print(f"Container '{container_name}' does not exist.")

    except docker.errors.APIError as e:
        print(f"Failed to start container: {e.explanation}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def is_container_running(container_name: str) -> bool:
    """Checks if a Docker container is currently running.

    Parameters
    ----------
    container_name : str
        Name of the container

    Returns
    -------
    bool
        True if the container is running, False otherwise.
    """
    try:
        client = docker.from_env()
        container = client.containers.get(container_name)

        # Refresh container status
        container.reload()

        return container.status == "running"

    except docker.errors.NotFound:
        print(f"Container '{container_name}' not found.")
        return False

    except Exception as e:
        print(f"Error checking container status: {e}")
        return False
