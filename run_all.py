import os

manager_path = r'./manager/main.py'
remote_gpt_path =r'./remote_gpt/run.py'
local_gpt_path = r'./local_gpt/run.py'
manim_path = r'manim/run.py'

os.system('python '+manager_path)
os.system('python '+remote_gpt_path)