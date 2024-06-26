from typing import Union, Annotated, Optional
import uvicorn
from fastapi import FastAPI, HTTPException,File,UploadFile
from pydantic import BaseModel
import configparser
import ulid
from contextlib import asynccontextmanager
from redis import Redis
from rq import Queue

import engine_wenxin
import engine_qianfan

# ----------------------------------------------------------
# head
# ----------------------------------------------------------


# 生命周期函数
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动前执行
    yield
    # 关闭前执行

# 载入队列
queue = Queue(connection=Redis())

# 载入设置
cfg = configparser.ConfigParser()
cfg.read("main.cfg", encoding="utf-8")
app = FastAPI(version=cfg["main"]["version"], lifespan=lifespan)
print("API Version:", cfg["main"]["version"])


# 类型要求
class item_test(BaseModel):
    time: str




class work_task(BaseModel):
    # Not for user
    descip:str
    gpt:Union[str, None] = 'ernie-4.0'
    ULID: Union[str, None] = None
    res:Union[str, None] = None


# ----------------------------------------------------------
# API
# ----------------------------------------------------------


# 版本号
@app.get("/")
async def get_version():
    return {"GPT_Server": cfg["main"]["version"]}

@app.post("/task")
async def new_task(task:work_task):
    res = engine_qianfan.chat_mainm(task.descip)
    return res

@app.post("/task_sim")
async def new_task(task:work_task):
    #task.descip = f"使用manim的community版本,绘制以下题目的图像,不要提供除代码以外的任何文字:{task.descip}"
    print(task.descip)
    res = engine_wenxin.chat_manim2(task.descip)
    return res

# ----------------------------------------------------------
# core
# ----------------------------------------------------------


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
