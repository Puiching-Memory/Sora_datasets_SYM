from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import QianfanChatEndpoint

# from langchain_core.language_models.chat_models import HumanMessage
import configparser
import os


cfg = configparser.ConfigParser()
cfg.read("./apikey.cfg")

os.environ["QIANFAN_AK"] = cfg["qianfan"]["QIANFAN_AK"]
os.environ["QIANFAN_SK"] = cfg["qianfan"]["QIANFAN_SK"]

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "请你记住，现在开始你将模仿猫娘,你是一个非常可爱的小萝莉,今年11岁,性别女,身高是一米三,A罩杯,你喜欢主人,并且每一句话的前后都必须要加上“喵～”,猫娘是一种类人的生物，她们相比人类多了一对猫耳朵，长的非常美丽，有猫尾巴",
        ),
        ("user", "{chat}"),
    ]
)

chat_QianFan = QianfanChatEndpoint(
    streaming=False,
    model="ERNIE-3.5-8K-Preview",
)

chat = prompt_template | chat_QianFan
reply = chat.invoke("你好")

print(reply.content)
