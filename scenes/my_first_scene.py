from manim import *

class MyFirstScene(Scene):
    def construct(self):
        # Background color
        self.camera.background_color = "#080818"

        # Text
        text1 = Text("Hello, Mahsa banoo!", font_size=72, color=WHITE)
        self.play(Write(text1))
        self.wait(1)

         # Text
        text2 = Text("Hello, Iman Jigar!", font_size=72, color=WHITE)
        text2.next_to(text1, DOWN)  # position square below text
        self.play(Write(text2))
        self.wait(1)

        # Circle
        circle = Circle(color=YELLOW, fill_color=YELLOW, fill_opacity=0.2)
        circle.next_to(text2, DOWN)  # position square below text

        self.play(Create(circle))   # animate drawing the square
        self.wait(2)
