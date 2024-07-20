from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.document_loaders import PyMuPDFLoader
# 旧版用法 # from langchain.document_loaders import UnstructuredFileLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import re
import pickle
import os

file_paths = []
folder_path = './knowledge'
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)
print(file_paths[0:])
model_name = r'/root/huggingface_cache/bce-embedding-base_v1'
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
a = open("documents.pkl","rb")
split_docs = pickle.load(a)
db = Chroma(persist_directory="./chroma/hacker_knowledge", embedding_function=hf)
db.add_documents(split_docs)
# 持久化
db.persist()