import os
import configparser
from typing import List, Literal
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.language_models.chat_models import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.base import BaseMessage
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.graph import END, MessageGraph
import requests

ABS_PATH = os.path.dirname(os.path.abspath(__file__))

cfg = configparser.ConfigParser()
cfg.read('./apikey.cfg')

os.environ["QIANFAN_AK"] = cfg['qianfan']['QIANFAN_AK']
os.environ["QIANFAN_SK"] = cfg['qianfan']['QIANFAN_SK']

def is_manim_work(state:List[BaseMessage]):
    SERVER_MANIM = 'http://127.0.0.1:5103'
    se1 = requests.post(SERVER_MANIM+'/task',json={'task':state[1].content})
    print(state[1].content)
    print(se1.json())
    if se1.json()['rencode'] == 0:
        return 'end'
    else:
        return 'continue'

def chat_mainm(ask:str):
    # Chat stream, integrated with LangChain
    chat_QianFan = QianfanChatEndpoint(
        streaming=False,
        model="ERNIE-3.5-8K",
    )
    builder = MessageGraph()
    builder.add_node("oracle", chat_QianFan)
    builder.add_conditional_edges(
    "oracle",
    is_manim_work,
    {
    "continue": "oracle",
    "end": END,
    },)

    builder.set_entry_point("oracle")
    runnable = builder.compile()

    reply = runnable.invoke(HumanMessage(f"{ask}"))
    print(reply)

    '''
    # input and output
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "依据用户提供的题目描述生成manim社区版本的python代码,生成的代码必须以一整段展示,不要尝试解释你生成的代码,不要为你的代码添加注释",
            ),
            ("user", "{input}"),
        ]
    )
    chain = prompt | chat_QianFan

    reply = chain.invoke(
    {
        "input": f"{ask}"
    }
    )
    print(reply.content)
    return reply.content
    '''

if __name__ == '__main__':
    chat_mainm('你好')