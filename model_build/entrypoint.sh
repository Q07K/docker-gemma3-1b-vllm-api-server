#!/bin/bash
set -e

API_KEY="$api_key"

exec vllm serve "./google/gemma-3-1b-it" --host "0.0.0.0" --port "8000" --api-key "$API_KEY" --dtype "half" --max-num-seqs "1" "$@"