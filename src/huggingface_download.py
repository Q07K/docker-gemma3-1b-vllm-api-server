"""Huggingface model downloader"""

from pathlib import Path

from huggingface_hub import login, snapshot_download


def save(repo_id: str, api_key: str | None = None) -> None:
    """Downloads a model from huggingface to a local directory.

    Parameters
    ----------
    repo_id : str
        repo_id of the model to download

    api_key : str | None, optional
       api key to use for huggingface, by default None
    """

    provider_name, model_name = repo_id.split("/")

    provider_name = Path(provider_name)
    model_name = Path(model_name)
    main_path = Path("model_build")

    model_path = main_path / provider_name / model_name

    if api_key:
        login(api_key)

    model_path = snapshot_download(
        repo_id=repo_id,
        local_dir=model_path,
        local_dir_use_symlinks=False,
    )
    print(f"Model downloaded to {model_path}")
