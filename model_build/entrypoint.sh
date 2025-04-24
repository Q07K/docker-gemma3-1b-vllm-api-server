#!/bin/bash
set -e

source /app/.venv/bin/activate

API_KEY="$api_key"

exec vllm serve "./google/gemma-3-1b-it" \
    --host "0.0.0.0" \
    --port "8000" \
    --api-key "$VLLM_API_KEY" \
    --max-num-seqs "1" \
    "$@"