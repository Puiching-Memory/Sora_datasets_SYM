"""
快速运行入口
此文件为热重载设计
"""

import os

current_work_dir = os.path.dirname(__file__) #当前文件路径

command = 'flet run -d ' + current_work_dir

print('执行命令:',command)
os.system(command=command)