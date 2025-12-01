"""
Exercise: Animate a Vector in 3D Space
Goal:
    Inside your template, create:
    A set of 3D axes
    A 3D vector starting at the origin and pointing to (1, 2, 1)
    A label for the vector, placed near its tip
    A simple animation:
    First show the label
    Then change the vector to point to (2, –1, 1)
    Move the label so it follows the new tip
    Do one camera rotation (azimuth or elevation)
"""
# Corrected code by ChatGPT############################

from manim import *
from manim.opengl import *

DEV_MODE = True

class LearningExercise3(ThreeDScene):

    # Organizing the scene construction into methods
    def construct(self):
        # 1. Camera setup + background
        self.set_up_camera()
        # 2. Creating main objects
        self.create_main_objects()
        # 3. Development checkpoint (interactive)
        if DEV_MODE:
            self.dev_checkpoint()
        # 4. Final animation sequence
        self.main_animation()
        # 5. Outro/hold final frame
        self.outro()

    def set_up_camera(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        self.camera.background_color = DARK_BLUE

    def create_main_objects(self):
        self.axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-6, 6, 1],
            z_range=[-7, 7, 1],
        )
        self.add(self.axes)


        x_label = self.axes.get_x_axis_label(MathTex("x"))
        y_label = self.axes.get_y_axis_label(MathTex("y"))
        z_label = self.axes.get_z_axis_label(MathTex("z"))

        x_label.rotate(PI/2, axis=RIGHT)
        y_label.rotate(PI/2, axis=RIGHT).rotate(PI/2, axis=UP).rotate(PI/4, axis=OUT)
       # z_label.rotate(PI/2, axis=)

        
      #  self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        self.add( x_label, y_label, z_label)

        self.vector1 = Arrow3D(
            start=ORIGIN,
            end=self.axes.c2p(1, 2, 1),
            color=GREEN,
        )
        self.label1 = MathTex(r"\vec{v_1}", color=YELLOW).next_to(
            self.vector1.get_end(), RIGHT + UP
        )

        self.vector2 = Arrow3D(
            start=ORIGIN,
            end=self.axes.c2p(2, -1, 1),
            color=GREEN,
        )
        self.label2 = MathTex(r"\vec{v_2}", color=YELLOW).next_to(
            self.vector2.get_end(), RIGHT + UP
        )

        # At the start we only show axes + first vector + first label
        self.add(self.axes, self.vector1, self.label1)

    def dev_checkpoint(self):
        self.interactive_embed()

    # Animation sequence
    def main_animation(self):
        # vector1 and label1 are already visible, but it's fine to animate them in
        self.play(Create(self.vector1))
        self.play(FadeIn(self.label1))
        self.wait(2)
        self.play(
            Transform(self.vector1, self.vector2),
            Transform(self.label1, self.label2),
        )
        self.wait(2)

    def outro(self):
        self.wait(2)


# My initial code ####################################
"""from manim import*
from manim.opengl import *

DEV_MODE = True

class LerningExercise3(ThreeDScene):

#Organizing the scene construction into methods
    def construct(self):
        #1.Camera setup + background
        self.set_up_camera()
        #2.Creating main objects
        self.create_main_objects()
        #3.Development checkpoint
        self.dev_checkpoint()
        #4.Final animation sequence
        self.main_animation()
        #5.Outro/hold final frame
        self.outro()

    def set_up_camera(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=45*DEGREES)
        self.camera.background_color = DARK_BLUE
    
    def create_main_objects(self):
        self.axes=ThreeDAxes(
            x_range=[-5,5,1],
            y_range=[-6,6,1],
            z_range=[-7,7,1]
        )
        self.vector1=Arrow3D(
            start=ORIGIN,
            end=self.axes.c2p(1,2,1),
            color=GREEN
        )
        self.label1=MathTex("\\vec{v_1}", color=YELLOW).next_to(self.vector1.get_end(), RIGHT+UP)
        self.vector2=Arrow3D(
            start=ORIGIN,
            end=self.axes.c2p(2,-1,1),
            color=GREEN
        )
        self.label2=MathTex("\\vec{v_2}", color=YELLOW).next_to(self.vector2.get_end(), RIGHT+UP)

        self.add(self.axes, self.vector1, self.label1)
        if DEV_MODE:
            self.interactive_embed()

        def dev_checkpoint(self):
            self.interactive_embed()

        def outro(self):
            self.wait(2)
    #Amination sequence
    def main_animation(self):
        self.play(Create(self.vector1))
        self.play(FadeIn(self.label1))
        self.wait(2)
        self.play(Transform(self.vector1, self.vector2), Transform(self.label1, self.label2))
        self.wait(2)
"""


