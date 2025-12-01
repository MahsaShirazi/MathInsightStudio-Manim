from manim import *
from manim.opengl import *

###############################################################################
# Manim Scene Workflow Template (Mahsa Shirazi/ Math Insight Studio)
#
# DEV USAGE (OpenGL, interactive):
#   manim --renderer=opengl -pql path/to/this_file.py EpisodeScene
#
# FINAL RENDER (no interactive, high quality):
#   1) Set DEV_MODE = False
#   2) Cairo (classic):
#        manim -pqh path/to/this_file.py EpisodeScene
#      or OpenGL:
#        manim --renderer=opengl -pqh path/to/this_file.py EpisodeScene
###############################################################################

DEV_MODE = True  # set to False for final video


class EpisodeScene(ThreeDScene):
    """
    Template for a YouTube episode scene.
    
    Rename this class to something meaningful per episode, e.g.:
        Ep01_IntroToLinearSystems
        Ep02_MatrixAsTransformation
    """

    def construct(self):
        # 1) Setup camera + background
        self.setup_camera()

        # 2) Create main objects (axes, vectors, planes, etc.)
        self.create_main_objects()

        # 3) (Optional) Development checkpoint for interactive tweaking
        if DEV_MODE:
            self.dev_checkpoint()

        # 4) Final animation sequence (what appears in the video)
        self.main_animation()

        # 5) Outro / hold final frame
        self.outro()

    # --------------------------------------------------------------------- #
    # SETUP METHODS
    # --------------------------------------------------------------------- #

    def setup_camera(self):
        """Initial camera and background settings."""
        # 3D camera orientation (adjust per episode)
        self.set_camera_orientation(phi=60 * DEGREES,theta=45 * DEGREES,frame_center=ORIGIN,zoom=1.0)
        # Background color (optional)
        self.camera.background_color = BLACK

    def create_main_objects(self):
        """Create and store the main objects as self.* so they are accessible in dev mode."""
        # Example: 3D axes
        self.axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-2, 2, 1],
        )

        # Example: a demo surface (replace with objects relevant to the episode)
        self.surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                0.2 * np.sin(u) * np.cos(v),
            ]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(16, 16),
        )
        self.surface.set_style(
            fill_opacity=0.6,
            stroke_width=1,
        )
        self.surface.set_color(BLUE_E)

        # Add everything you want visible at the start:
        self.add(self.axes, self.surface)

        # TODO: for your episodes, create things like:
        #   self.vector = Arrow3D(ORIGIN, RIGHT + UP + OUT)
        #   self.plane = Rectangle(...).rotate(...)
        #   self.label = MathTex("Ax = b").to_corner(UL)

    # --------------------------------------------------------------------- #
    # DEV CHECKPOINT
    # --------------------------------------------------------------------- #

    def dev_checkpoint(self):
        """
        Interactive development checkpoint.

        When DEV_MODE = True and you run with OpenGL, this will:
          - keep the window open
          - give you an `In [1]:` prompt in the terminal
        So you can try things like:

            self.surface.set_color(RED)
            self.renderer.update_frame()

            self.play(self.surface.animate.shift(UP))
            self.play(self.camera.animate.set_elevation(30*DEGREES))
        """
        self.interactive_embed()

    # --------------------------------------------------------------------- #
    # MAIN ANIMATION (FINAL VIDEO CONTENT)
    # --------------------------------------------------------------------- #

    def main_animation(self):
        """The actual narrative animation that will be in the final video."""

        # Example sequence – REPLACE this with your real episode logic.
        self.play(Create(self.axes))
        self.play(FadeIn(self.surface))
        self.wait(0.5)

        # TODO: put your real story here:
        #   - introduce question
        #   - animate vectors / planes / matrices
        #   - show key equations with MathTex
        #   - use camera moves to emphasize geometry

        # Example camera move:
        self.play(self.camera.animate.set_azimuth(75 * DEGREES), run_time=2)
        self.play(self.camera.animate.set_elevation(45 * DEGREES), run_time=2)
        self.wait(1)

    # --------------------------------------------------------------------- #
    # OUTRO
    # --------------------------------------------------------------------- #

    def outro(self):
        """Hold final frame, add end text, or fade out."""
        # Example: hold the last frame for 2 seconds
        self.wait(2)

        # TODO: optional outro text/logo, e.g.:
        #   outro_text = Text("MathInsight Studio", font_size=36).to_corner(DR)
        #   self.play(FadeIn(outro_text))
        #   self.wait(1)
        #   self.play(FadeOut(VGroup(self.axes, self.surface, outro_text)))
        #   self.wait(0.5)
