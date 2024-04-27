import requests

data = {'descip':'使用manim社区版,绘制以下题目的图像:圆O半径r=3,点P为圆O上一动点,连接OP'}
re = requests.post('http://localhost:5102/task',json=data)

print(re.json())