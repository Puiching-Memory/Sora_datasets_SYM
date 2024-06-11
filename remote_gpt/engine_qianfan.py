import os
import configparser
from typing import List
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.language_models.chat_models import HumanMessage
#from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.base import BaseMessage
#from langchain_core.tools import tool
#from langgraph.prebuilt import ToolNode
from langgraph.graph import END, MessageGraph
import requests

ABS_PATH = os.path.dirname(os.path.abspath(__file__))

cfg = configparser.ConfigParser()
cfg.read("./apikey.cfg")

os.environ["QIANFAN_AK"] = cfg["qianfan"]["QIANFAN_AK"]
os.environ["QIANFAN_SK"] = cfg["qianfan"]["QIANFAN_SK"]

global error_report
error_report = ""


def is_manim_work(state: List[BaseMessage]):
    SERVER_MANIM = "http://127.0.0.1:5103"
    se1 = requests.post(SERVER_MANIM + "/task", json={"task": state[-1].content})
    #print(state, len(state))
    print(se1.json())
    # state.append(HumanMessage(''))
    if se1.json()["rencode"] == 0:
        return "end"
    else:
        global error_report
        error_report = str(se1.json()['error'])
        return "continue"


def add_enpty(state: List[BaseMessage]):
    return HumanMessage(f"依据报错修改你的代码,保持你一开始的回复格式,仅提供你修改过后的代码:{error_report}")


def chat_mainm(ask: str):
    # Chat stream, integrated with LangChain
    chat_QianFan = QianfanChatEndpoint(
        streaming=False,
        model="ERNIE-4.0-8K-Preview",
    )
    builder = MessageGraph()
    builder.add_node("oracle", chat_QianFan)
    builder.add_node("enpty", add_enpty)
    builder.add_conditional_edges(
        "oracle",
        is_manim_work,
        {
            "continue": "enpty",
            "end": END,
        },
    )
    builder.add_edge("enpty", "oracle")

    builder.set_entry_point("oracle")
    runnable = builder.compile()

    reply = runnable.invoke(HumanMessage(f"{ask}"))
    print(reply)


if __name__ == "__main__":
    chat_mainm(
        "依据用户提供的题目描述生成manim社区版本的python代码,生成的代码必须以一整段展示,不要尝试解释你生成的代码,不要为你写的代码添加注释："
        + "画一个圆O,点P为圆O上一个点,连接OP为一条直线。"
        +"额外要求:如果是动点,那么需要体现其动态效果。"
    )
