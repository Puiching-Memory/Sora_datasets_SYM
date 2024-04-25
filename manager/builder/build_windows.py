"""
windows平台构建脚本
"""

import os

current_work_dir = os.path.dirname(__file__)  # 当前文件路径
root_dir = os.path.abspath(os.path.join(current_work_dir, os.path.pardir))  # 当前文件上一级目录
app_dir = root_dir + "\\main.py"  # main.py所在路径

#可调参数#
output_dir = root_dir + '\\release' # 生成文件夹
build_number = 100 # 构建版本数字
build_version = f"{'.'.join(str(build_number))}" # 构建版本字符串
template_dir = r"D:\GitHub\Sora_datasets_SYM\manager\flet-build-template" # 模板路径
include_packages = 'flet_video' #额外包


command = (f"flet build windows {root_dir}"
           + f' --template {template_dir}'
           #+ f' --include-packages {include_packages}'
           #+ f' --output {output_dir}'
           #+ f' --build-number {build_number}'
           #+ f' --build-version {build_version}'
           )

print("执行命令:", command)
os.system(command=command)
