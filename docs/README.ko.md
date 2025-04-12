# docker-gemma3-1b-vllm-api-server

[![English](https://img.shields.io/badge/Language-English-blue)](README.md)
![Korean](https://img.shields.io/badge/Language-한국어-gray)
[![日本語](https://img.shields.io/badge/Language-日本語-blue)](/docs/README.ja.md)

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-v3.10-blue?logo=python)](https://www.python.org/)
[![Python Package Manager](https://img.shields.io/badge/Package_Manager-uv-blue)](https://docs.astral.sh/uv/)
[![Version](https://img.shields.io/badge/Version-0.1.0-orange)](https://github.com/teddylee777/langgraph-mcp-agents)

---

## 시작하기

### 1. `gemma-3-1b-it` 모델 다운로드
- 링크: [HuggingFace - gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it)

### 2. `uv` 설치 (Python 패키지 관리자)
- 설치 가이드: [uv 설치 문서](https://docs.astral.sh/uv/getting-started/installation/)

#### 3. `.env` 파일 생성
```env
HUGGINGFACE_API_KEY = "hf_..."
API_KEY = "..."
```

### 4. 의존성 동기화
```sh
uv sync
```

### 5. 가상 환경 활성화

- **Windows**
    ```sh
    .\.venv\Scripts\activate
    ```
- **Linux**
    ```sh
    source .venv/bin/activate
    ```

### 6. 초기화 스크립트 실행
```sh
python init_run.py
```

## Docker 설정

### 1. `model_build` 디렉토리로 이동
```sh
cd ./model_build
```

### 2. Docker 이미지 빌드
```sh
docker build -t gemma3-1b:v1.0.0 .
```

### 3. Docker 컨테이너 실행
```sh
docker run --gpus all -i -t -p 8000:8000 -e api_key="..." gemma3-1b:v1.0.0
```

## API 서버 실행
```sh
python main.py
```

## GPU 정보

|속성|값|
|---|---|
|모델명|NVIDIA GeForce RTX 2060|
|총 메모리|12,288 MiB (12 GB)|
|드라이버 버전|561.09|
|CUDA 버전|12.6|
|드라이버 모델|WDDM (Windows Display Driver Model)|


### `nvidia-smi` 출력
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