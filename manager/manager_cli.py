"""
管理器CLI版本
"""

import requests
import os
import shutil
import sys
from loguru import logger

SERVER_REMOTE = 'http://127.0.0.1:5102'
SERVER_MANIM = 'http://127.0.0.1:5103'
SERVER_STASH = 'http://127.0.0.1:5104'
TASK_PATH = './test_data.txt'

def init():
    #初始化
    se1 = is_server_online(SERVER_REMOTE)
    se2 = is_server_online(SERVER_MANIM)
    return f'远程GPT{se1}|manim执行器{se2}'

def is_server_online(url:str):
    #检查指定URL的服务器是否在线
    if url == '': raise IndexError('url不能为空')
    re = requests.get(url+'/')
    return re

def load_task(task_file_path:str):
    #从txt载入自动任务
    with open(task_file_path,encoding='utf8') as file:
        file = file.readlines()
        file = [i.replace('\n','') for i in file]

    return file

def gen_code(url:str,task:str):
    #执行提示生成代码
    se1 = requests.post(url+'/task',json={'descip':task})
    print(se1.json())
    return se1.json()

def gen_vedio(url:str,code:str):
    #执行从代码生成视频
    se1 = requests.post(url+'/task',json={'task':code})
    return se1.text

if __name__ == '__main__':
    logger.info(f'初始化,检查服务器链接:{init()}')
    task_list = load_task(TASK_PATH)
    logger.info(f'加载自动任务:{len(task_list)}')

    for task in task_list:
        code = gen_code(SERVER_REMOTE,task)
        logger.info(f'执行:{task},{code}')

        vedio_path = gen_vedio(SERVER_MANIM,code)
        logger.info(f'执行:{task},{vedio_path}')


        

    