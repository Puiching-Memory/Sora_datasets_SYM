import erniebot

# List supported models
models = erniebot.Model.list()

print(models)
# ernie-bot             文心一言旗舰版
# ernie-bot-turbo       文心一言轻量版
# ernie-text-embedding  文心百中语义模型
# ernie-vilg-v2         文心一格模型

# Set authentication params
erniebot.api_type = "aistudio"
erniebot.access_token = "<access-token-for-aistudio>"

# Create a chat completion
response = erniebot.ChatCompletion.create(model="ernie-bot", messages=[{"role": "user", "content": "你好，请介绍下你自己"}])

print(response.result)