import erniebot
import configparser
import requests

apikey = configparser.ConfigParser()
apikey.read("apikey.cfg", encoding="utf-8")
apikey = apikey['main']['key']

# List supported models
models = erniebot.Model.list()

#print(models)
# ernie-bot             文心一言旗舰版
# ernie-bot-turbo       文心一言轻量版
# ernie-text-embedding  文心百中语义模型
# ernie-vilg-v2         文心一格模型

# Set authentication params
erniebot.api_type = "aistudio"
erniebot.access_token = apikey

# Create a chat completion
def chat_wenxin4(ask:str,model:str):
    response = erniebot.ChatCompletion.create(model=model, messages=[{"role": "user", "content": ask,"system":'你是为帮助用户使用manim社区版本制作动画的助手。不要使用Python代码以外的任何内容进行响应。'}])

    #print(response.result)
    
    return response.result