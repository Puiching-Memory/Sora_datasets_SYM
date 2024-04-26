import manim

class Circle(manim.Circle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_stroke(manim.colors.BLUE)

def main():
    scene = manim.Scene()
    circle = Circle(radius=1, center=(0, 0))
    scene.add(circle)
    scene.render()

if __name__ == "__main__":
    main()