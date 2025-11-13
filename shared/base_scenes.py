"""
Base scene classes for the Manim project with common settings.
Use these as base classes for your scenes to avoid repetition.
"""
from manim import *

class BaseScene(Scene):
    """Base 2D scene with project defaults."""
    def construct(self):
        self.camera.background_color = "#09091E" 

class Base3DScene(ThreeDScene):
    """Base 3D scene with OpenGL defaults.
    Subclasses should call super().construct() at the END of their construct() method
    to keep the window open indefinitely.
    """
    def keep_window_open(self):
        """Call this at the end of your construct() to keep the window open."""
        self.wait(float('inf'))