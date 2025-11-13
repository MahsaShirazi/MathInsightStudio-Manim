# scenes/opengl_test.py
from manim import *

class OpenGLTest(ThreeDScene):
    def construct(self):
        print("Using renderer:", self.renderer.__class__.__name__)
        self.set_camera_orientation(phi=70*DEGREES, theta=45*DEGREES)
        axes = ThreeDAxes()
        cube = Cube(side_length=2, fill_opacity=0.1, stroke_color=YELLOW)
        self.add(axes, cube)
        self.begin_ambient_camera_rotation(rate=0.2)
        # Window stays open until manually closed (via manim.cfg preview setting)
        self.wait()
