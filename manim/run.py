###用于Nuitka打包,并未在该文件内使用
from typing import Union, Annotated, Optional
import uvicorn
from fastapi import FastAPI, HTTPException,File,UploadFile
from pydantic import BaseModel
import configparser
import ulid
from contextlib import asynccontextmanager
from redis import Redis
from rq import Queue
###

import uvicorn
import subprocess

# import configargparse
import configparser

cfg = configparser.ConfigParser()
cfg.read("main.cfg",encoding='utf-8')

def main():
    uvicorn.run(
        app="main:app",
        host='127.0.0.1',#'127.0.0.1'
        port=int(cfg["main"]["port"]),
        reload=eval(cfg["main"]["reload"]),
        workers=int(cfg["main"]["workers"]),
    )

def rq_run_worker():
    # 启动rq执行器
    command = ('rq worker --with-scheduler')

    process = subprocess.Popen(command, shell=True)
    return process

if __name__ == "__main__":
    #rq_run_worker()
    main()
