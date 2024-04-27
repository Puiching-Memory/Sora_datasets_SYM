import erniebot
import configparser
import requests

apikey = configparser.ConfigParser()
apikey.read("apikey.cfg", encoding="utf-8")
apikey = apikey['main']['key']

# List supported models
models = erniebot.Model.list()

print(models)
# ernie-bot             文心一言旗舰版
# ernie-bot-turbo       文心一言轻量版
# ernie-text-embedding  文心百中语义模型
# ernie-vilg-v2         文心一格模型

# Set authentication params
erniebot.api_type = "aistudio"
erniebot.access_token = apikey

# Create a chat completion
response = erniebot.ChatCompletion.create(model="ernie-4.0", messages=[{"role": "user", "content": "使用manim社区版本,画一个圆O,有一个动点P在O上移动,连接PO"}])

print(response.result)