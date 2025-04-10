**English** | [한국어](/docs/README.ko.md) | [日本語](/docs/README.ja.md)

---

# docker-gemma3-1b-vllm-api-server

## Run

### Download `gemma-3-1b-it`

1. **Access model:** https://huggingface.co/google/gemma-3-1b-it

1. **Install uv:** https://docs.astral.sh/uv/getting-started/installation/

1. **Synchronize Dependencies**
    ```
    uv sync
    ```

1. **Create `.env`**
    ```
    HUGGINGFACE_API_KEY = "hf_ur..."
    API_KEY = "..."
    ```

1. **Run `init_run.py`**
    ```shell
    python init_run.py
    ```

### Docker
1. **move to `./model_build`**
    ```
    cd ./model_build
    ```

1. **Build Docker image**
    ```shell
    docker build -t gemma3-1b:v1.0.0 .
    ```

1. **Run Docker image**
    ```
    docker run --gpus all -i -t -p 8000:8000 -e api_key="..."  gemma3-1b:v1.0.0
    ```

### Call API

1. **Run `main.py`**
    ```
    python main.py
    ```

## GPU Information

* **Model Name:** NVIDIA GeForce RTX 2060
* **Total Memory:** 12288 MiB (12 GB)
* **NVIDIA Driver Version:** 561.09
* **CUDA Version:** 12.6
* **Driver Model:** WDDM (Windows Display Driver Model)

### `nvidia-smi` Output
```shell
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 561.09                 Driver Version: 561.09         CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                  Driver-Model | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 2060      WDDM  |   00000000:01:00.0  On |                  N/A |
| 30%   41C    P8             13W /  184W |   10563MiB /  12288MiB |      4%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```