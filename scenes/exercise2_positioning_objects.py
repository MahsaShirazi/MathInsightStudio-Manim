from manim import *

class PositionDemo(Scene):
    def construct(self):
        self.camera.background_color = "#080818"

        # Text at the top
        title = Text("Positioning Demo", font_size=60, color=WHITE)
        title.to_edge(UP)  # move to top edge
        self.play(Write(title))
        self.wait(1)

        # Circle in the middle
        circle = Circle(color="#00FFFF", fill_opacity=0.4)
        self.play(Create(circle))
        self.wait(1)

        # Square below the circle
        square = Square(color=YELLOW, fill_opacity=0.4)
        square.next_to(circle, DOWN, buff=0.5)  # buff adds spacing
        self.play(Create(square))
        self.wait(1)

        # Triangle to the right of the circle
        triangle = RegularPolygon(3, color=GREEN, fill_opacity=0.4)
        triangle.next_to(circle, RIGHT, buff=0.5)
        self.play(Create(triangle))
        self.wait(2)
