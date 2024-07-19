#!/bin/bash

cd ./hackerllm_fastapi
# 激活 Conda 环境
source activate llm

# 运行 Python 脚本
nohup python main.py > output.log 2>&1 &