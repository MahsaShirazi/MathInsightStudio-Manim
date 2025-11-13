from manim import *

# Colors
#COL_OAT  = TEAL_D
#COL_YOG  = BLUE_D
#COL_RASP = RED_D
#COL_TGT  = PURPLE_C
#COL_ROW  = ORANGE
#COL_COL  = GREEN_D

BG = "#080818"

# Per cup vectors (cal, protein, sugar)
OAT_VEC  = [120, 3, 7]
YOG_VEC  = [90, 21, 1]
RASP_VEC = [64, 1, 5]
TGT_VEC  = [394, 28, 24]
# ------------------------------------------------------------------------------
#Motivation example: Healthy smoothie recipe as linear system
# ------------------------------------------------------------------------------
class IntroMotivationExample(Scene):
    """
    Sequence:
      1) Names centered, then move to top-left and shrink. Add "1 cup" under each.
      2) Build 3x3 nutrient table under each ingredient: (cal, prot, sugar) as rows.
      3) Fade in Target column to the right with (394,28,24).
      4) Highlight ingredient columns (building blocks), then highlight target column when asking "can they build the target?"
      5) Transform "1 cup" -> x_1, x_2, x_3 (under each ingredient).
      6) Multiply each column's entries by its x_i, one column at a time (for narration pacing).
      7) Add plus signs row-wise and show equals to target; then highlight rows (rules) and columns (building blocks).
    """
    def construct(self):
        self.camera.background_color = BG

        # ---------- 1) Ingredient names centered ----------
        title = Text("Healthy Smoothie", font_size=60).to_edge(UP)
        self.play(FadeIn(title, run_time=0.6))

        oat_name  = Text("Oat milk", font_size=38, color=YELLOW)
        yog_name  = Text("Greek yogurt", font_size=38, color=BLUE)
        rasp_name = Text("Raspberries", font_size=38, color=RED)
        names_center = VGroup(oat_name, yog_name, rasp_name).arrange(DOWN, buff=0.35).move_to(ORIGIN+UP*0.3)

        self.play(LaggedStart(FadeIn(oat_name), FadeIn(yog_name), FadeIn(rasp_name), lag_ratio=0.2, run_time=1.0))
        self.wait(0.6)

        # Plan final top-left positions (grid anchor)
        # Anchor: top-left region for the header row (names + "1 cup")
        header_left = LEFT*5.2 + UP*2.1  # tweak if needed
        x_gap = 3.1
        y_gap = 0.45

        # Prepare "1 cup" labels to appear under each name after moving
        cup_oat  = Text("1 cup", font_size=32, color=YELLOW)
        cup_yog  = Text("1 cup", font_size=32, color=BLUE)
        cup_rasp = Text("1 cup", font_size=32, color=RED)

        # Target column header (fades later)
        tgt_label = Text("Target smoothie", font_size=36, color=PURPLE)

        # Move names to header row (top-left), shrink a bit, then show "1 cup" under each
        names_top = VGroup(
            oat_name.copy().scale(0.8).move_to(header_left + RIGHT*0*x_gap + DOWN*0*y_gap),
            yog_name.copy().scale(0.8).move_to(header_left + RIGHT*1*x_gap + DOWN*0*y_gap),
            rasp_name.copy().scale(0.8).move_to(header_left + RIGHT*2*x_gap + DOWN*0*y_gap),
        )
        self.play(Transform(oat_name, names_top[0]), Transform(yog_name, names_top[1]), Transform(rasp_name, names_top[2]), run_time=0.9)
        self.play(
            FadeIn(cup_oat.next_to(oat_name, DOWN, buff=0.12)),
            FadeIn(cup_yog.next_to(yog_name, DOWN, buff=0.12)),
            FadeIn(cup_rasp.next_to(rasp_name, DOWN, buff=0.12)),
            run_time=0.6
        )

        # ---------- 2) Nutrient rows under each ingredient ----------
        row_labels = VGroup(
            Text("calories", font_size=30),
            Text("protein (g)", font_size=30),
            Text("sugar (g)", font_size=30),
        ).arrange(DOWN, buff=y_gap).move_to(header_left + LEFT*1.65 + DOWN*1.45)

        # Helper: make a column of numbers with highlight
        def make_col(vec, color, col_index):
            entries = VGroup(
                MathTex(str(vec[0]), color=color),
                MathTex(str(vec[1]), color=color),
                MathTex(str(vec[2]), color=color),
            ).arrange(DOWN, buff=y_gap)
            # place under the corresponding header (oat/yog/rasp)
            anchor = header_left + RIGHT*col_index*x_gap + DOWN*1.5
            entries.move_to(anchor)
            return entries

        col_oat  = make_col(OAT_VEC,  YELLOW,  0)
        col_yog  = make_col(YOG_VEC,  BLUE,  1)
        col_rasp = make_col(RASP_VEC, RED, 2)

        # Show row labels and columns; briefly highlight entries column-by-column
        self.play(FadeIn(row_labels, shift=RIGHT, run_time=0.5))
        self.play(LaggedStart(Write(col_oat[0]), Write(col_oat[1]), Write(col_oat[2]), lag_ratio=0.2, run_time=0.8))
        self.play(Indicate(col_oat, color=YELLOW), run_time=0.6)

        self.play(LaggedStart(Write(col_yog[0]), Write(col_yog[1]), Write(col_yog[2]), lag_ratio=0.2, run_time=0.8))
        self.play(Indicate(col_yog, color=BLUE), run_time=0.6)

        self.play(LaggedStart(Write(col_rasp[0]), Write(col_rasp[1]), Write(col_rasp[2]), lag_ratio=0.2, run_time=0.8))
        self.play(Indicate(col_rasp, color=RED), run_time=0.6)

        # Put simple headers (Oat milk (1 cup), etc.) above the numeric columns as a compact label line
        header_oat  = Text("Oat milk (1 cup)", font_size=26, color=YELLOW).next_to(col_oat, UP, buff=0.2)
        header_yog  = Text("Greek yogurt (1 cup)", font_size=26, color=BLUE).next_to(col_yog, UP, buff=0.2)
        header_rasp = Text("Raspberries (1 cup)", font_size=26, color=RED).next_to(col_rasp, UP, buff=0.2)
        self.play(FadeIn(header_oat), FadeIn(header_yog), FadeIn(header_rasp), run_time=0.6)

        # ---------- 3) Target column fades in ----------
        tgt_header_pos = header_left + RIGHT*3.3*x_gap + DOWN*0.02  # a bit to the right with margin
        tgt_label.move_to(tgt_header_pos)
        tgt_col = VGroup(
            MathTex(str(TGT_VEC[0]), color=PURPLE),
            MathTex(str(TGT_VEC[1]), color=PURPLE),
            MathTex(str(TGT_VEC[2]), color=PURPLE),
        ).arrange(DOWN, buff=y_gap).move_to(tgt_header_pos + DOWN*1.6)

        self.play(FadeIn(tgt_label, shift=UP, run_time=0.5))
        self.play(LaggedStart(Write(tgt_col[0]), Write(tgt_col[1]), Write(tgt_col[2]), lag_ratio=0.2, run_time=0.8))
        self.play(Indicate(tgt_col, color=PURPLE), run_time=0.6)

        # ---------- 4) Highlight columns as building blocks, then target ----------
        blocks_box = SurroundingRectangle(VGroup(col_oat, col_yog, col_rasp), color=GREEN, buff=0.2)
        self.play(Create(blocks_box), run_time=0.5)
        self.wait(0.2)
        self.play(FadeOut(blocks_box), run_time=0.3)

        tgt_box = SurroundingRectangle(VGroup(tgt_label, tgt_col), color=PURPLE, buff=0.25)
        self.play(Create(tgt_box), run_time=0.5)
        self.wait(0.2)
        self.play(FadeOut(tgt_box), run_time=0.3)

        # ---------- 5) Turn "1 cup" -> x_1, x_2, x_3 ----------
        x1 = MathTex("x_1", color=YELLOW).scale(1.0).move_to(cup_oat.get_center())
        x2 = MathTex("x_2", color=BLUE).scale(1.0).move_to(cup_yog.get_center())
        x3 = MathTex("x_3", color=RED).scale(1.0).move_to(cup_rasp.get_center())
        self.play(Transform(cup_oat, x1), Transform(cup_yog, x2), Transform(cup_rasp, x3), run_time=0.8)

        # ---------- 6) Multiply each ingredient column by its x_i (one at a time) ----------
        # Create scaled columns (symbolic multiplication display)
        col_oat_scaled = VGroup(
            MathTex(f"{OAT_VEC[0]}\\,x_1", color=YELLOW),
            MathTex(f"{OAT_VEC[1]}\\,x_1", color=YELLOW),
            MathTex(f"{OAT_VEC[2]}\\,x_1", color=YELLOW),
        ).arrange(DOWN, buff=y_gap).move_to(col_oat)

        col_yog_scaled = VGroup(
            MathTex(f"{YOG_VEC[0]}\\,x_2", color=BLUE),
            MathTex(f"{YOG_VEC[1]}\\,x_2", color=BLUE),
            MathTex(f"{YOG_VEC[2]}\\,x_2", color=BLUE),
        ).arrange(DOWN, buff=y_gap).move_to(col_yog)

        col_rasp_scaled = VGroup(
            MathTex(f"{RASP_VEC[0]}\\,x_3", color=RED),
            MathTex(f"{RASP_VEC[1]}\\,x_3", color=RED),
            MathTex(f"{RASP_VEC[2]}\\,x_3", color=RED),
        ).arrange(DOWN, buff=y_gap).move_to(col_rasp)

        # Animate one column at a time for narration pacing
        self.play(TransformMatchingTex(col_oat, col_oat_scaled), Indicate(x1, color=YELLOW), run_time=0.9)
        self.wait(0.1)
        self.play(TransformMatchingTex(col_yog, col_yog_scaled), Indicate(x2, color=BLUE), run_time=0.9)
        self.wait(0.1)
        self.play(TransformMatchingTex(col_rasp, col_rasp_scaled), Indicate(x3, color=RED), run_time=0.9)

        # ---------- 7) Row-wise addition and equality to target ----------
        # Plus signs between columns for each row
        plus_row1 = MathTex("+", color=WHITE).move_to(col_yog_scaled[0].get_left() + LEFT*0.5).align_to(col_yog_scaled[0], DOWN)
        plus_row2 = MathTex("+", color=WHITE).move_to(col_yog_scaled[1].get_left() + LEFT*0.5).align_to(col_yog_scaled[1], DOWN)
        plus_row3 = MathTex("+", color=WHITE).move_to(col_yog_scaled[2].get_left() + LEFT*0.5).align_to(col_yog_scaled[2], DOWN)

        plus2_row1 = MathTex("+", color=WHITE).move_to(col_rasp_scaled[0].get_left() + LEFT*0.5).align_to(col_rasp_scaled[0], DOWN)
        plus2_row2 = MathTex("+", color=WHITE).move_to(col_rasp_scaled[1].get_left() + LEFT*0.5).align_to(col_rasp_scaled[1], DOWN)
        plus2_row3 = MathTex("+", color=WHITE).move_to(col_rasp_scaled[2].get_left() + LEFT*0.5).align_to(col_rasp_scaled[2], DOWN)

        self.play(FadeIn(plus_row1), FadeIn(plus_row2), FadeIn(plus_row3), run_time=0.5)
        self.play(FadeIn(plus2_row1), FadeIn(plus2_row2), FadeIn(plus2_row3), run_time=0.5)

        # Equality signs before target column (one per row)
        eq1 = MathTex("=", color=WHITE).next_to(tgt_col[0], LEFT, buff=0.55)
        eq2 = MathTex("=", color=WHITE).next_to(tgt_col[1], LEFT, buff=0.55)
        eq3 = MathTex("=", color=WHITE).next_to(tgt_col[2], LEFT, buff=0.55)
        self.play(FadeIn(eq1), FadeIn(eq2), FadeIn(eq3), run_time=0.5)

        # Highlight rows (rules)
        row1_box = SurroundingRectangle(VGroup(col_oat_scaled[0], plus_row1, col_yog_scaled[0], plus2_row1, col_rasp_scaled[0], eq1, tgt_col[0]), 
                                        color=ORANGE, buff=0.15)
        row2_box = SurroundingRectangle(VGroup(col_oat_scaled[1], plus_row2, col_yog_scaled[1], plus2_row2, col_rasp_scaled[1], eq2, tgt_col[1]), 
                                        color=ORANGE, buff=0.15)
        row3_box = SurroundingRectangle(VGroup(col_oat_scaled[2], plus_row3, col_yog_scaled[2], plus2_row3, col_rasp_scaled[2], eq3, tgt_col[2]), 
                                        color=ORANGE, buff=0.15)
        self.play(Create(row1_box), run_time=0.4)
        self.play(Indicate(row1_box, color=ORANGE), run_time=0.5)
        self.play(Create(row2_box), run_time=0.4)
        self.play(Indicate(row2_box, color=ORANGE), run_time=0.5)
        self.play(Create(row3_box), run_time=0.4)
        self.play(Indicate(row3_box, color=ORANGE), run_time=0.5)

        # Highlight columns (building blocks)
        col_oat_box  = SurroundingRectangle(VGroup(header_oat, x1, col_oat_scaled), color=GREEN, buff=0.18)
        col_yog_box  = SurroundingRectangle(VGroup(header_yog, x2, col_yog_scaled), color=GREEN, buff=0.18)
        col_rasp_box = SurroundingRectangle(VGroup(header_rasp, x3, col_rasp_scaled), color=GREEN, buff=0.18)
        self.play(Create(col_oat_box), run_time=0.4)
        self.play(Indicate(col_oat_box, color=GREEN), run_time=0.5)
        self.play(Create(col_yog_box), run_time=0.4)
        self.play(Indicate(col_yog_box, color=GREEN), run_time=0.5)
        self.play(Create(col_rasp_box), run_time=0.4)
        self.play(Indicate(col_rasp_box, color=GREEN), run_time=0.5)

        # Footer message
        footer = Tex(r"\textbf{Rows = rules \qquad Columns = building blocks $\rightarrow$ target }").scale(0.8).to_edge(DOWN)
        self.play(FadeIn(footer, shift=UP, run_time=0.5))
        self.wait(0.8)
# ------------------------------------------------------------------------------
#Introduction to linear equations and systems
# ------------------------------------------------------------------------------