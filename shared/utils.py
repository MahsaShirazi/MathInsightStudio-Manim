from manim import *

def set_zoom(scene, zoom_value):
    """
    Sets the camera zoom level for both Cairo and OpenGL renderers.
    Usage: set_zoom(self, 0.7)
    """
    cam = scene.renderer.camera
    if hasattr(cam, "set_zoom"):
        cam.set_zoom(zoom_value)
    else:
        cam.zoom = zoom_value
