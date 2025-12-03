from manim import *
from manim.opengl import *

class RotatingThreeDCoordinate(ThreeDScene):
    
    def construct (self):

        # Set up 3D axes
        self.axes = ThreeDAxes(
            x_range = [-5,5,1],
            y_range = [-5,5,1],
            z_range = [-5,5,1]
        )
        self.add(self.axes)
    
        # Set up camera orientation and background
        self.set_camera_orientation(phi = 60*DEGREES, theta = 45*DEGREES)
        self.camera.background_color = "#080818"

        # Set up axes labels
        x_label = MathTex("x")
        y_label = MathTex("y")
        z_label = MathTex("z")

        #Place labels at the end of each axis
        x_label.move_to(self.axes.c2p(self.axes.x_range[1]+0.5,0,0))
        y_label.move_to(self.axes.c2p(0,self.axes.y_range[1]+0.5,0))
        z_label.move_to(self.axes.c2p(0,0,self.axes.z_range[1]+0.5))

        # Ensure labels facethe camera during rotation
        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        
        # Play animation to rotate the camera around the z-axes
        self.begin_ambient_camera_rotation(rate=0.1)
        #self.interactive_embed()
        self.wait(10)
        self.stop_ambient_camera_rotation()

