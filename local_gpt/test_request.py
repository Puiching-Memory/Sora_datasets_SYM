import requests


data = {
    "model": "Llama3-8B-Chinese-Chat",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "只使用manim,绘制一个圆形,不要分步提供代码"},
    ],
}
re = requests.post("http://localhost:8080/v1/chat/completions", json=data)

re_json = re.json()
print(re_json)
print(re_json['choices'][0]['message']['content'])