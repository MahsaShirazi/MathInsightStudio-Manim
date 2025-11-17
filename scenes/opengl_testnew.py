from manim import *
from manim.opengl import *


class OpenGLTest(ThreeDScene):
    def construct(self):
        # Axes
        axes = ThreeDAxes()

        # A simple 3D surface (a bump) so you see depth
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                0.2 * np.sin(u) * np.cos(v),
            ]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(16, 16),
        )
        surface.set_style(fill_opacity=0.6, stroke_width=1)

        # Set initial camera angle
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        self.add(axes, surface)

        # 🔑 This keeps the window open and gives you an interactive console
        self.interactive_embed()
