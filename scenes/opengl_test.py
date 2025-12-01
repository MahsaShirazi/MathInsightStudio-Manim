# scenes/opengl_test.py
from manim import *
from manim.opengl import *

DEV_MODE = False  # set to False for final video

class OpenGLTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=45*DEGREES)

        self.axes = ThreeDAxes()
        self.cube = Cube(side_length=2, fill_opacity=0.1, stroke_color=YELLOW)
        self.cube.set_style(fill_opacity=0.6, stroke_width=1)
        self.add(self.axes, self.cube)
    
        # Window stays open until manually closed (via manim.cfg preview setting)
        if DEV_MODE:
            self.interactive_embed()

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(10)
