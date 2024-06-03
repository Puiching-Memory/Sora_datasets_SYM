import os
import subprocess
import ulid
import time


def save_file(task: str):
    task_id = ulid.ULID.from_timestamp(time.time())
    os.mkdir("./cache/" + str(task_id))
    cache_dir = "./cache/" + str(task_id)

    with open(cache_dir + "/task.py",'w',encoding='utf-8') as file:
        file.write(task)

    return cache_dir + "/task.py"


def ren(path: str,clsa:str):
    command = "manim" + " -pqh" + f" {path} {clsa}"
    print(command)
    result = subprocess.run(["manim", "-pqh",path,clsa], capture_output=True, text=True,encoding='gbk')
    print(result.stdout,result.returncode,result.stderr)

    return result


def decode(ins: str):
    #寻找python代码
    index_s = ins.find("```python")
    index_e = ins.rfind("```")

    cut = ins[index_s + 10 : index_e]

    #移除if main代码
    index_s = cut.find('if __name__ == "__main__":')

    cut = cut[:index_s]

    #寻找class名称
    clsa = cut[cut.find('class') + 6:]
    clsa = clsa[:clsa.find('(')]

    return cut,clsa


if __name__ == "__main__":
    ask = """
使用manim社区版,绘制以下题目的图像:圆O半径r=3,点P为圆O上一动点,连接OP


`manim` 是一个用于制作数学动画的库，它基于 Python 和 LaTeX。要使用 `manim` 社区版来绘制您所描述的图像，您需要首先安装 `manim`，然后编写一个脚本来描述您想要的动画。

以下是一个基本的 `manim` 脚本示例，用于绘制一个半径为 3 的圆，并在圆上移动一个点 P，同时始终保持 OP 连接：

```python
from manim import *

class CircleAndPoint(Scene):
    def construct(self):
        # 创建圆 O
        circle = Circle(radius=3)
        circle.set_color(BLUE)
        circle_label = Tex("O")
        circle_label.move_to(circle.get_center())

        # 创建点 P
        point_P = Dot(color=RED)
        point_P.move_to(circle.point_at_angle(0))  # 初始位置设置为圆上的某个点
        point_label = Tex("P")
        point_label.next_to(point_P, UP)

        # 创建 OP 线段
        line_OP = Line(circle.get_center(), point_P.get_center())
        line_OP.set_color(GREEN)

        # 将所有对象添加到场景中
        self.add(circle, circle_label)
        self.play(ShowCreation(line_OP))
        self.play(ShowCreation(point_P), ShowCreation(point_label))

        # 让点 P 在圆上移动
        for angle in range(0, 360, 10):
            point_P.move_to(circle.point_at_angle(angle * DEGREES))
            line_OP.become(Line(circle.get_center(), point_P.get_center()))
            self.play(MoveTarget(point_P), MoveTarget(line_OP))

        # 保持场景在屏幕上
        self.wait()

# 运行脚本
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -c '#2B2B2B' --video_dir ~/Downloads/ "
    command_B = module_name + " CircleAndPoint -pl"
    os.system(command_A + command_B)
```

请注意，上面的代码可能需要根据您的 `manim` 版本和安装情况进行一些调整。特别是，`manim` 的 API 在不同版本之间可能会有所变化。

这个脚本创建了一个蓝色的圆，一个红色的点 P，以及一个绿色的线段 OP。然后，它使点 P 在圆上移动，并始终保持 OP 连接。

要运行此脚本，请将其保存为 `.py` 文件，并确保您已经安装了 `manim` 社区版。然后，您可以通过命令行运行此脚本，它将生成一个视频文件，您可以在任何支持的视频播放器中查看。

另外，请注意，我在上面的脚本中添加了一个 `if __name__ == "__main__":` 块来运行动画。这是 Python 的一种常见做法，用于指示当脚本作为主程序运行时应该执行哪些代码。这样，如果您将此脚本导入到其他脚本中，它不会自动运行动画。

此外，`os.system(command_A + command_B)` 这一行可能需要根据您的操作系统和 `manim` 的安装位置进行调整。我假设您已经将 `manim` 安装在了系统的 PATH 中，并且您想要将生成的视频保存到 `~/Downloads/` 目录中。如果您的情况不同，请相应地修改这些值。
"""

    re,re2 = decode(ask)

    print(re,re2)
