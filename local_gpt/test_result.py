import manim

class Example(manim.Scene):
    def construct(self):
        circle = manim.Circle(
            center=[0, 0],
            radius=1,
            stroke_width=2
        )
        self.add(circle)

if __name__ == "__main__":
    m = Example()
    m.render()