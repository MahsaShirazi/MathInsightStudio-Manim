from manim import *

class ProjectionIntro(Scene):
    def construct(self):
        title = Text("Vector Projection", font_size=60)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 4, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_tip": True},
        ).to_edge(LEFT).shift(RIGHT*0.5)

        self.play(Create(axes))

        # Define vectors u and v
        u = Vector([4, 2], color=BLUE).shift(axes.c2p(0, 0) - ORIGIN)
        v = Vector([3, 1], color=YELLOW).shift(axes.c2p(0, 0) - ORIGIN)

        u_label = Text("u", font_size=36, color=BLUE).next_to(u.get_end(), UR, buff=0.1)
        v_label = Text("v", font_size=36, color=YELLOW).next_to(v.get_end(), UR, buff=0.1)

        self.play(GrowArrow(u), FadeIn(u_label, shift=UP*0.2))
        self.play(GrowArrow(v), FadeIn(v_label, shift=UP*0.2))
        self.wait(0.3)

        # Projection of u onto v
        v_dir = v.get_end() - v.get_start()
        u_end = u.get_end() - u.get_start()
        proj_len = np.dot(u_end, v_dir) / np.dot(v_dir, v_dir)
        proj_vec = Vector(proj_len * v_dir, color=GREEN).shift(axes.c2p(0,0) - ORIGIN)

        proj_label = Text("proj_v(u)", font_size=30, color=GREEN)            .next_to(proj_vec.get_end(), DOWN, buff=0.15)

        # Helper dashed line from u tip to projection tip
        helper = DashedLine(u.get_end(), proj_vec.get_end(), dash_length=0.1, color=GRAY_B)

        self.play(GrowArrow(proj_vec), FadeIn(proj_label, shift=DOWN*0.2))
        self.play(Create(helper))
        self.wait(0.5)

        note = Text("Idea: shadow of u on v", font_size=28, slant=ITALIC)            .to_edge(DOWN)
        self.play(Write(note))
        self.wait(1)

class ProjectionFormula(Scene):
    def construct(self):
        title = Text("Projection Formula", font_size=60)
        self.play(Write(title)); self.wait(0.4); self.play(FadeOut(title))

        # Requires LaTeX installed for MathTex
        formula = MathTex(
            r"\mathrm{proj}_{\mathbf v}\mathbf u = "
            r"\frac{\mathbf u\cdot\mathbf v}{\lVert \mathbf v \rVert^2} \mathbf v",
            font_size=56
        )
        self.play(Write(formula))
        self.wait(1)

        # Highlight pieces
        num = formula.get_part_by_tex("\mathbf u\cdot\mathbf v")
        den = formula.get_part_by_tex("\lVert \mathbf v \rVert^2")
        vecv = formula.get_part_by_tex("\mathbf v")

        self.play(num.animate.set_color(YELLOW))
        self.play(den.animate.set_color(RED))
        self.play(vecv.animate.set_color(GREEN))
        self.wait(1.2)
