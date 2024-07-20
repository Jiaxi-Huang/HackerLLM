# HackerLLM

[![](https://img.shields.io/github/watchers/ToughMamba/HackerLLM.svg?style=flat)](https://github.com/PKUanonym/REKCARC-TSC-UHT/watchers)
[![](https://img.shields.io/github/stars/ToughMamba/HackerLLM.svg?style=flat)](https://github.com/PKUanonym/REKCARC-TSC-UHT/stargazers)
[![](https://img.shields.io/github/forks/ToughMamba/HackerLLM.svg?style=flat)](https://github.com/PKUanonym/REKCARC-TSC-UHT/network/members)
[![](https://img.shields.io/github/issues-pr-closed-raw/ToughMamba/HackerLLM.svg?style=flat)](https://github.com/PKUanonym/REKCARC-TSC-UHT/issues)
![](https://img.shields.io/github/repo-size/ToughMamba/HackerLLM.svg?style=flat)

WebPage: http://47.109.104.63/index

## 简介

本项目基于vue(前端)以及fastapi(后端),通过调用bce-embedding模型进行向量数据库文本嵌入，结合到prompt调用通义前文qwen-long长对话模型，实现特定领域的问答。同时vue引入vuetify组件实现对https://www.hackthebox.com 网站的分析结果进行可视化展示

## 运行
适用于ubuntu linux(也适用于windows本地运行)
- 安装anaconda/miniconda并初始化
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```
- 下载项目需要的python库，主要是dashscope,langchain,fastapi,chromadb等，有报错缺少xx，直接pip install xx就好
- 安装node.js(不必要)
```bash
sudo apt-get update 
sudo apt-get install nodejs
```
- 申请模型api_key
详见https://help.aliyun.com/zh/dashscope/
至少截至24年7月免费额度还是挺多的

并且在`main.py`中配置api_key，详见：
https://help.aliyun.com/zh/dashscope/developer-reference/acquisition-and-configuration-of-api-key?spm=a2c4g.11186623.0.0.42124937yljUMp
- 下载huggingface模型
下载地址: https://huggingface.co/maidalun1020/bce-embedding-base_v1/tree/main
下载好后在`main.py`中更改代码段
```py
model_name = r"/root/huggingface_cache/bce-embedding-base_v1"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hfembedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
```
将model_name改为你下载好后放的路径

## 贡献
SWS3023 Web Mining Group1
- Li Lanzhe
- Zhu Ziyi
- Wang Yuyu
- Huang Yuhao
- Huang Jiaxi

**Welcome pull request**
