from fastapi import FastAPI,WebSocket,Request, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dashscope import Generation
from http import HTTPStatus
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
import uvicorn
import logging
from fastapi.staticfiles import StaticFiles
app = FastAPI()
# 配置日志
logging.basicConfig(level=logging.INFO)
#配置RAG
model_name = r"/root/huggingface_cache/bce-embedding-base_v1"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hfembedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
db = Chroma(persist_directory="./chroma/hacker_knowledge", embedding_function=hfembedding)

# 配置CORS
origins = [
    "http://47.109.104.63"
    "http://47.109.104.63:80",#公网ip
]

app.mount("/index", StaticFiles(directory="./dist/index/", html=True), name="index")
app.mount("/css", StaticFiles(directory="./dist/index/css/", html=True), name="css")
app.mount("/fonts", StaticFiles(directory="./dist/index/fonts/", html=True), name="fonts")
app.mount("/js", StaticFiles(directory="./dist/index/js/", html=True), name="js")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

message_histories = {}


@app.post("/api")
async def qwen_response(request: Request):
    try:
        # 获取请求头中的IP地址
        ip = request.headers.get("x-forwarded-for") or request.headers.get("x-real-ip") or request.client.host
        print(ip)
        # 检查IP是否已经存在，如果不存在则初始化message_history
        if ip not in message_histories:
            message_histories[ip] = [{'role': 'system', 'content': "你是一个网络安全知识助手"}]

        question_request = await request.json()
        prompt_text = question_request.get("question")
        similarDocs = db.max_marginal_relevance_search(prompt_text, k=5)
        summary_prompt = "\n".join([doc.page_content for doc in similarDocs])
        send_message = f""" 
        历史对话：{message_histories[ip]}
        你可以在需要时通过 '---' 之间的上下文内容对用户问题的答案进行完善
        用户问题：{prompt_text}
        ---
        {summary_prompt}
        ---
        如果你认为上下文与问题无关，请简要回答。
        """
        message_histories[ip].append({'role': 'user', 'content': send_message})
        response = Generation.call(model='qwen-14b-chat', result_format='message', messages=message_histories[ip])
        if response.status_code == HTTPStatus.OK:
            message_histories[ip].append(({'role': response.output.choices[0]['message']['role'],
                                          'content': response.output.choices[0]['message']['content']}))
            return {"response": response.output.choices[0]['message']['content']}
        else:
            return {"status_code": response.status_code}
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8886)