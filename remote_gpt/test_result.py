from manim import *
import os

class CircleTangentPoint(Scene):
    def construct(self):
        # 创建一个圆O
        circle = Circle(radius=1, color=BLUE)
        circle.move_to(ORIGIN)
        self.add(circle)

        # 创建一个点O表示圆心
        dot_o = Dot(color=YELLOW)
        dot_o.move_to(ORIGIN)
        self.add(dot_o)

        # 创建一个切线A
        line_a = Line(LEFT*2, UP, color=RED)
        line_a.rotate(TAU/4, about_point=ORIGIN)  # 假设切线A与x轴呈45度角
        self.add(line_a)

        # 创建一个动点P在A上移动
        dot_p = Dot(color=GREEN)
        dot_p.move_to(line_a.get_start())
        self.add(dot_p)

        # 创建一个线段PO连接圆心和动点
        line_po = Line(ORIGIN, dot_p.get_center(), color=PURPLE)
        self.add(line_po)

        # 让动点P在A上移动，并更新线段PO
        self.play(
            MoveAlongPath(dot_p, line_a),
            UpdateFromAlphaFunc(line_po, lambda m, a: line_po.become(Line(ORIGIN, dot_p.get_center()))),
            run_time=3
        )

        # 停留一会儿
        self.wait()

# 运行脚本
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -c '#2B2B2B' --video_dir ~/Downloads/ "
    command_B = module_name + " CircleTangentPoint -pl"
    os.system(command_A + command_B)