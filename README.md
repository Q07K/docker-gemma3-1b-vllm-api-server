# docker-gemma3-1b-vllm-api-server

![English](https://img.shields.io/badge/Language-English-gray)
[![Korean](https://img.shields.io/badge/Language-한국어-blue)](/docs/README.ko.md)
[![日本語](https://img.shields.io/badge/Language-日本語-blue)](/docs/README.ja.md)

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-v3.10-blue?logo=python)](https://www.python.org/)
[![Python Package Manager](https://img.shields.io/badge/Package_Manager-uv-blue)](https://docs.astral.sh/uv/)
[![Version](https://img.shields.io/badge/Version-0.1.0-orange)](https://github.com/teddylee777/langgraph-mcp-agents)

---

## Getting Started

### 1. Request access to `gemma-3-1b-it` model
- Visit: [HuggingFace - gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it)
- Click **"Access repository"** and agree to the terms for usage.

### 2. Install `uv` (Python package manager)
- Guide: [uv Installation Docs](https://docs.astral.sh/uv/getting-started/installation/)

### 3. Create `.env` file
```
HUGGINGFACE_API_KEY = "hf_..."
API_KEY = "..."
```

### 4. Sync dependencies
```
uv sync
```

### 5. Activate the virtual environment

- **Windows**
    ```sh
    .\.venv\Scripts\activate
    ```
- **Linux**
    ```sh
    source .venv/bin/activate
    ```

### 6. Run initialization script
```shell
python init_run.py
```



## Docker Setup

### 1. Navigate to `model_build` directory
```
cd ./model_build
```

### 2. Build Docker image
```shell
docker build -t gemma3-1b:v1.0.0 .
```

### 3. Run Docker container
```
docker run --gpus all -i -t -p 8000:8000 -e api_key="..." gemma3-1b:v1.0.0
```

## API Usage
To start the API server, simply run:
```
python main.py
```

## GPU Information

|Property|Value|
|---|---|
|Model Name|NVIDIA GeForce RTX 2060|
|Total Memory|12,288 MiB (12 GB)|
|Driver Version|561.09|
|CUDA Version|12.6|
|Driver Model|WDDM (Windows Display Driver Model)|


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
