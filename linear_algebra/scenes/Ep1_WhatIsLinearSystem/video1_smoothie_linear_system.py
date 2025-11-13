from manim import *

# Colors
OAT_COLOR  = TEAL_D
YOG_COLOR  = BLUE_D
RASP_COLOR = RED_D
RULES_COLOR = ORANGE
BUILD_COLOR = GREEN_D
B_COLOR = PURPLE_C

class Video1_Steps1to6_Clean(Scene):
    def construct(self):
        self.camera.background_color = "#0e0f12"

        # ---------- ZONE: Title ----------
        title = Text("Healthy Smoothie — Linear System", weight=BOLD, font_size=42)
        title.to_edge(UP)
        self.play(FadeIn(title, shift=DOWN, run_time=0.6))

        # ---------- ZONE A (top): Ingredients + x1,x2,x3 ----------
        # icons (simple dots) + labels
        oat = VGroup(Dot(color=OAT_COLOR).scale(1.2), Text("Oat milk", font_size=32)).arrange(DOWN, buff=0.2)
        yog = VGroup(Dot(color=YOG_COLOR).scale(1.2), Text("Greek yogurt", font_size=32)).arrange(DOWN, buff=0.2)
        rsp = VGroup(Dot(color=RASP_COLOR).scale(1.2), Text("Raspberries", font_size=32)).arrange(DOWN, buff=0.2)

        ing_row = VGroup(oat, yog, rsp).arrange(RIGHT, buff=1.6)
        ing_row.next_to(title, DOWN, buff=0.6)

        # variables under each
        x1 = MathTex("x_1\\ \\text{cups}", color=OAT_COLOR).scale(0.9).next_to(oat, DOWN, buff=0.25)
        x2 = MathTex("x_2\\ \\text{cups}", color=YOG_COLOR).scale(0.9).next_to(yog, DOWN, buff=0.25)
        x3 = MathTex("x_3\\ \\text{cups}", color=RASP_COLOR).scale(0.9).next_to(rsp, DOWN, buff=0.25)

        top_block = VGroup(ing_row, x1, x2, x3)
        self.play(LaggedStart(FadeIn(oat), FadeIn(yog), FadeIn(rsp), lag_ratio=0.15, run_time=0.8))
        self.play(FadeIn(x1), FadeIn(x2), FadeIn(x3), run_time=0.6)
        self.wait(0.2)

        # ---------- ZONE B (bottom-left): Targets panel ----------
        targets = VGroup(
            Text("Targets", font_size=30, weight=BOLD),
            Text("383 calories", font_size=28),
            Text("28 g protein", font_size=28),
            Text("24 g sugar", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        targets_panel = SurroundingRectangle(targets, color=WHITE, buff=0.3)
        targets_group = VGroup(targets_panel, targets).scale(0.95)
        targets_group.to_edge(LEFT).to_edge(DOWN).shift(UP*0.3 + RIGHT*0.2)

        self.play(Create(targets_panel), FadeIn(targets, lag_ratio=0.1), run_time=0.8)
        self.wait(0.2)

        # ---------- Fade top visuals slightly before equations ----------
        self.play(top_block.animate.set_opacity(0.6), run_time=0.4)

        # ---------- ZONE C (right side): Row picture box ----------
        row_title = Text("Row picture (rules/constraints)", font_size=28, color=RULES_COLOR)
        row_eqs = VGroup(
            MathTex("c_o x_1 + c_y x_2 + c_r x_3 = 383", color=RULES_COLOR),
            MathTex("p_o x_1 + p_y x_2 + p_r x_3 = 28",  color=RULES_COLOR),
            MathTex("s_o x_1 + s_y x_2 + s_r x_3 = 24",  color=RULES_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.9)

        row_box = VGroup(row_title, row_eqs).arrange(DOWN, buff=0.25)
        row_box.scale(0.95)
        row_box.to_edge(RIGHT).shift(LEFT*0.3 + UP*0.2)

        underline = Line(row_title.get_left(), row_title.get_right(), color=RULES_COLOR, stroke_width=3).next_to(row_title, DOWN, buff=0.1)

        self.play(FadeIn(row_title, shift=UP, run_time=0.4), Create(underline, run_time=0.3))
        self.play(LaggedStart(Write(row_eqs[0]), Write(row_eqs[1]), Write(row_eqs[2]), lag_ratio=0.15, run_time=1.2))
        self.wait(0.2)

        # ---------- ZONE D (bottom-center/right): Column picture (A x = b) ----------
        col_title = Text("Column picture (building blocks → target b)", font_size=28, color=BUILD_COLOR)

        A = MathTex(
            r"\begin{bmatrix}"
            r"c_o & c_y & c_r\\"
            r"p_o & p_y & p_r\\"
            r"s_o & s_y & s_r"
            r"\end{bmatrix}", color=BUILD_COLOR
        ).scale(0.9)
        x_vec = MathTex(r"\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}").scale(0.9)
        eq = MathTex("=")
        b_vec = MathTex(r"\begin{bmatrix}383\\28\\24\end{bmatrix}", color=B_COLOR).scale(0.9)

        Ax_eq_b = VGroup(A, x_vec, eq, b_vec).arrange(RIGHT, buff=0.35)
        col_group = VGroup(col_title, Ax_eq_b).arrange(DOWN, buff=0.25).scale(0.95)

        # place column group below row_box, centered between row_box and targets_group
        # compute a middle x between left and right blocks to avoid overlap
        midpoint_x = (targets_group.get_right()[0] + row_box.get_left()[0]) / 2
        col_group.move_to([midpoint_x, targets_group.get_top()[1] + 0.4, 0])

        self.play(FadeIn(col_title, shift=UP, run_time=0.4))
        self.play(Write(Ax_eq_b), run_time=1.0)

        # arrows from columns of A to b (visual cue only)
        col1_src = A.get_left() + RIGHT*0.9 + UP*0.55
        col2_src = A.get_left() + RIGHT*0.9
        col3_src = A.get_left() + RIGHT*0.9 + DOWN*0.55

        col_mid = b_vec.get_left() + LEFT*0.25
        arr1 = Arrow(col1_src, col_mid + UP*0.25, buff=0.05, stroke_width=3, color=OAT_COLOR)
        arr2 = Arrow(col2_src, col_mid,               buff=0.05, stroke_width=3, color=YOG_COLOR)
        arr3 = Arrow(col3_src, col_mid + DOWN*0.25,   buff=0.05, stroke_width=3, color=RASP_COLOR)
        self.play(Create(arr1), Create(arr2), Create(arr3), run_time=0.7)

        # ---------- ZONE E (footer message) ----------
        msg = Tex(r"\textbf{Rows = rules \quad\quad Columns = building blocks $\rightarrow$ target $\mathbf{b}$.}")
        msg.scale(0.85).to_edge(DOWN).shift(UP*0.2)
        self.play(FadeIn(msg, shift=UP, run_time=0.5))
        self.wait(1.0)
