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
        self.camera.background_color = DARK_BLUE

        # Set up axes labels
        x_label = MathTex("x")
        y_label = MathTex("y")
        z_label = MathTex("z")

        x_label.move_to(self.axes.c2p(self.axes.x_range[1]+0.5,0,0))
        y_label.move_to(self.axes.c2p(0,self.axes.y_range[1]+0.5,0))
        z_label.move_to(self.axes.c2p(0,0,self.axes.z_range[1]+0.5))

        #x_label.rotate(PI/2, axis=RIGHT)
        #y_label.rotate(PI/2, axis=RIGHT).rotate(PI/2, axis=UP).rotate(PI/4, axis=OUT)

        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        #self.add(x_label, y_label, z_label)

        self.begin_ambient_camera_rotation(rate=0.1)
        

        self.interactive_embed()

        self.wait(10)
        self.stop_ambient_camera_rotation()

