from typing import Union, Annotated, Optional
import uvicorn
from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
import configparser
import ulid
from contextlib import asynccontextmanager
from redis import Redis
from rq import Queue

import engine_manim

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


class item_task(BaseModel):
    task: str


# ----------------------------------------------------------
# API
# ----------------------------------------------------------


# 版本号
@app.get("/")
async def get_version():
    return {"manim_Server": cfg["main"]["version"]}


@app.post("/task")
async def new_task(task: item_task):
    cut, clsa = engine_manim.decode(task.task)
    file_path = engine_manim.save_file(cut)
    result = engine_manim.ren(file_path, clsa)
    if result.returncode == 1:
        return {"rencode": 1, "error": result.stderr}
    else:
        return {"rencode": 0, "path": file_path, "clsa": clsa}


# ----------------------------------------------------------
# core
# ----------------------------------------------------------


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
