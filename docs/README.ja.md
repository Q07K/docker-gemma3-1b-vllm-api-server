# docker-gemma3-1b-vllm-api-server

[![English](https://img.shields.io/badge/Language-English-blue)](/README.md)
[![Korean](https://img.shields.io/badge/Language-한국어-blue)](/docs/README.ko.md)
![日本語](https://img.shields.io/badge/Language-日本語-gray)

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-v3.10-blue?logo=python)](https://www.python.org/)
[![Python Package Manager](https://img.shields.io/badge/Package_Manager-uv-blue)](https://docs.astral.sh/uv/)
[![Version](https://img.shields.io/badge/Version-0.1.0-orange)](https://github.com/teddylee777/langgraph-mcp-agents)

---


## はじめに

### 1. `gemma-3-1b-it` モデルのダウンロード
- Visit: [HuggingFace - gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it)

### 2. `uv` (Python package manager)のインストール
- Guide: [uv Installation Docs](https://docs.astral.sh/uv/getting-started/installation/)

### 3. `.env` ファイルの作成
```
HUGGINGFACE_API_KEY = "hf_..."
API_KEY = "..."
```

### 4. 依存関係の同期
```
uv sync
```

### 5. 仮想環境をアクティベート

- **Windows**
    ```sh
    .\.venv\Scripts\activate
    ```
- **Linux**
    ```sh
    source .venv/bin/activate
    ```

### 6. 初期化スクリプトの実行
```shell
python init_run.py
```



## Docker セットアップ

### 1. `model_build` ディレクトリに移動
```
cd ./model_build
```

### 2. Docker イメージのビルド
```shell
docker build -t gemma3-1b:v1.0.0 .
```

### 3. Docker コンテナの起動
```
docker run --gpus all -i -t -p 8000:8000 -e api_key="..." gemma3-1b:v1.0.0
```

## API の使い方
API サーバーを起動するには、以下のコマンドを実行してください：
```
python main.py
```

## GPU 情報

|項目|値|
|---|---|
|モデル名|NVIDIA GeForce RTX 2060|
|搭載メモリ|12,288 MiB (12 GB)|
|ドライババージョン|561.09|
|CUDA バージョン|12.6|
|ドライバモデル|WDDM (Windows Display Driver Model)|


### `nvidia-smi` 出力例
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
