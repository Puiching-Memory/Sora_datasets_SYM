from manim import *

class CircleAndPoint(Scene):
    def construct(self):
        # 创建一个圆 O
        circle = Circle(color=BLUE)
        circle.set_fill(opacity=0.5)
        circle_label = Tex("O")
        circle_label.move_to(circle.get_center())

        # 创建一个动点 P
        dot = Dot(color=RED)
        dot.move_to(circle.point_at_angle(0))  # 初始位置设为圆的最右侧点
        dot_label = Tex("P")
        dot_label.next_to(dot, DOWN)

        # 创建一个始终连接圆心和动点的线段
        line = Line(circle.get_center(), dot.get_center(), color=YELLOW)

        # 添加所有元素到场景中
        self.add(circle, circle_label, dot, dot_label, line)

        # 让动点 P 在圆上移动
        self.play(
            Rotate(dot, angle=2 * PI, about_point=circle.get_center(), rate_func=linear),
            UpdateFromFunc(line, lambda m: m.become(Line(circle.get_center(), dot.get_center()))),
            run_time=5
        )

        # 暂停动画
        self.wait()

        # 可选：让动点 P 回到初始位置
        self.play(
            Rotate(dot, angle=-2 * PI, about_point=circle.get_center(), rate_func=linear),
            UpdateFromFunc(line, lambda m: m.become(Line(circle.get_center(), dot.get_center()))),
            run_time=5
        )

        # 移除所有元素
        # self.clear()

# 运行动画
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -c '#2B2B2B' --video_dir ~/Downloads/ "
    command_B = module_name + " CircleAndPoint -pl"
    os.system(command_A + command_B)