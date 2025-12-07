from manim import *
from manim.opengl import *

DEV_MODE = True  # set to False for final video

# Colors
#COL_OAT  = TEAL_D
#COL_YOG  = BLUE_D
#COL_RASP = RED_D
#COL_TGT  = PURPLE_C
#COL_ROW  = ORANGE
#COL_COL  = GREEN_D

BG ="#080818"\

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
      1) Make a 3x3 nutrient table, rows labeled (calories, protein, sugar),
         Columns labelled (Oat milk, Greek yogurt, Raspberries). But first show the column
         names alone at the top. Then add "1 cup" under each name, simultaneously. 
         Then show the row labels on the left.
      2) Fill in each ingredient column one at a time with its nutrient values.
      3) Fade in Target column to the right with (394,28,24) one at a time, so that it matches 
         the row labels by highlighting 394 together with "calories", etc.
         Highlight target column when asking "can they build the target?" 

         Say: In other words, is there x-1, x-2, x-3 such that the ingredients combine to the target? Meaning that if I have:
      4) Change the first column header to "Oat milk (x_1 cup)", add empty ovals around each column and  multiply by x_1. 
         Animate this for each column: change header to include x_i. 
      5) Add plus signs between the ovals arounf the columns and add equal sign with a question mark on top of that, to target; 
         Say: columns as (building blocks)
      6) now, show the row picture by removing the ovals around the columns and then multiplying x_is to each column's entries, 
         adding plus between row enteries and equal sign to target entry. 
         
      7) Then highlight each row as a "rule" that must be satisfied.
      8) Now remove all row boxes anf the highligths from the columns. And fade out the labels or make them more transparent. 
         What we are left with is a linear system. Fade in a footer message: A linear system
    """
    def construct(self):
        self.camera.background_color = BG

        # ---------- 1) Ingredient names centered ----------
        title = Text("Healthy Smoothie", font_size=60).to_edge(UP)
        self.play(FadeIn(title, run_time=0.6))

        oat_name  = Text("Oat milk", font_size=38, color=YELLOW)
        yog_name  = Text("Greek yogurt", font_size=38, color=BLUE)
        rasp_name = Text("Raspberries", font_size=38, color=RED)
        names_center = VGroup(oat_name, yog_name, rasp_name).arrange(  RIGHT, buff=0.5).move_to(ORIGIN+UP*0.9)

        self.play(LaggedStart(FadeIn(oat_name), FadeIn(yog_name), FadeIn(rasp_name), lag_ratio=0.2, run_time=1.0))
        self.wait(0.6)

        if DEV_MODE:
            self.interactive_embed()

        # Plan final top-left positions (grid anchor)
        # Anchor: top-left region for the header row (names + "1 cup")
        header_left = LEFT*5 + UP*2.1  # tweak if needed
        x_gap = 2.1
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

        if DEV_MODE:
            self.interactive_embed()

        # ---------- 2) Nutrient rows under each ingredient ----------
        row_labels = VGroup(
            Text("calories", font_size=20),
            Text("protein (g)", font_size=20),
            Text("sugar (g)", font_size=20),
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

        tgt_box = SurroundingRectangle(VGroup(tgt_label, tgt_col), color=PURPLE, buff=0.20)
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
# Motivation example: Healthy smoothie recipe as linear system
# ------------------------------------------------------------------------------
class IntroMotivationExample_v2(Scene):
    """
    Sequence:
      1) Make a 3x3 nutrient table, rows labeled (calories, protein, sugar),
         Columns labelled (Oat milk, Greek yogurt, Raspberries). But first show the column
         names alone at the top.
         Then show the row labels on the left.
      2) Then add "1 cup" under the first name. Fill in the ingredient column  of the first column with its nutrient values. Repeat this for the other two columns
      3) Fade in Target column to the right with (394,28,24) one at a time, so that it matches 
         the row labels by highlighting 394 together with "calories", etc.
         Highlight target column when asking "can they build the target?" 

         Say: In other words, is there x_1, x_2, x_3 such that the ingredients combine to the target?
      4) Change column headers to include x_i, add empty ovals around each column and think of
         each column as being multiplied by x_i. Animate this for each column.
      5) Add plus signs between the ovals around the columns and add an equal sign with a 
         question mark on top of that, pointing to the target; say: columns as "building blocks".
      6) Now, show the row picture by removing the ovals around the columns and then multiplying
         x_i to each column's entries, adding plus between row entries and equal sign to each
         target entry. 
      7) Then highlight each row as a "rule" that must be satisfied.
      8) Now remove all row boxes and the highlights from the columns. And fade out the labels
         or make them more transparent. What we are left with is a linear system.
         Fade in a footer message: "A linear system".
    """

    def construct(self):
        self.camera.background_color = BG

        # Ingredient names centered ------------------------------
        title = Text("Healthy Smoothie", font_size=60).to_edge(UP)
        self.play(FadeIn(title, run_time=0.6))

        oat_name  = Text("Oat milk", font_size=20, color=YELLOW)
        yog_name  = Text("Greek yogurt", font_size=20, color=BLUE)
        rasp_name = Text("Raspberries", font_size=20, color=RED)
        names_center = VGroup(oat_name, yog_name, rasp_name).arrange(
            RIGHT, buff=0.5
        ).move_to(ORIGIN+LEFT*0.5 + UP * 0.9)

        self.play(FadeIn(names_center, lag_ratio=0.2, run_time=1.0))

        self.wait(0.6)

        #if DEV_MODE:
        #    self.interactive_embed()

        # Row labels --------------------------------------------------------------
        row_labels = VGroup(
            Text("calories", font_size=20),
            Text("protein (g)", font_size=20),
            Text("sugar (g)", font_size=20),
        ).arrange(DOWN, buff= 0.45, aligned_edge=LEFT).move_to(
            LEFT * 5.7 + DOWN * 1.25
        )

        self.play(FadeIn(row_labels, shift=RIGHT, run_time=0.5))

        # Prepare "1 cup" labels
        cup_oat  = Text("1 cup", font_size=20, color=YELLOW)
        cup_yog  = Text("1 cup", font_size=20, color=BLUE)
        cup_rasp = Text("1 cup", font_size=20, color=RED)


        # Helper: make a nutrient column
        def make_col(vec, color, col_index):
            entries = VGroup(
                MathTex(str(vec[0]), color=color),
                MathTex(str(vec[1]), color=color),
                MathTex(str(vec[2]), color=color),
            ).arrange(DOWN, buff=0.45)
            return entries

        col_oat  = make_col(OAT_VEC,  YELLOW, 0)
        col_yog  = make_col(YOG_VEC,  BLUE,   1)
        col_rasp = make_col(RASP_VEC, RED,    2)

        #Show nutrition column for oat-----------------------------------------------
        self.play(
            FadeIn(cup_oat.next_to(oat_name, DOWN, buff=0.12)),
            run_time=0.6,
        )

        self.play(
            FadeIn(col_oat.next_to(cup_oat, DOWN, buff=0.6)), run_time=0.6
        )

        #Show nutrition column for yogurt-------------------------------------------
        self.play(
            FadeIn(cup_yog.next_to(yog_name, DOWN, buff=0.12)),
            run_time=0.6,
        )

        self.play(
            FadeIn(col_yog.next_to(cup_yog, DOWN, buff=0.6)), run_time=0.6
        )

        #Show nutrition column for raspberry----------------------------------------
        self.play(
            FadeIn(cup_rasp.next_to(rasp_name, DOWN, buff=0.12)),
            run_time=0.6,
         )

        self.play(
            FadeIn(col_rasp.next_to(cup_rasp, DOWN, buff=0.6)), run_time=0.6
        )

        # Show Target column ---------------------------------------------------------
        tgt_label = VGroup(
            Text("Target", font_size=20, color=PURPLE),
            Text("smoothie", font_size=20, color=PURPLE)
        ).arrange(DOWN, buff=0.09)
        tgt_label.next_to(rasp_name, RIGHT, buff=0.5).shift(DOWN*0.2)
        
        tgt_col = make_col(TGT_VEC, PURPLE, 3)

        self.play(FadeIn(tgt_label, run_time=0.5))
        self.play(FadeIn(tgt_col.next_to(tgt_label, DOWN, buff=0.6)), run_time=0.6)
        #----------------------------------------------------------------------------
        # Up until here is good and no need for changes
        #----------------------------------------------------------------------------

    # 1) Fade out title, show question, highlight target column
        question = Text(
            "Can the ingredients be scaled to match the target?",
            font_size=26
        ).to_edge(UP)

        self.play(FadeOut(title, run_time=0.5))
        self.play(FadeIn(question, shift=UP, run_time=0.8))

        self.play(
            Indicate(
                VGroup(tgt_label, tgt_col),
                color=PURPLE,
                scale_factor=1.05
            ),
            run_time=1.0
        )

        # 2) Change "1 cup" -> "x_1 cup", add rounded rectangle and x_1
        cup_oat_x = MathTex(r"x_1\ \text{cup}", color=YELLOW)
        cup_oat_x.next_to(oat_name, DOWN, buff=0.12)

        self.play(ReplacementTransform(cup_oat, cup_oat_x), run_time=0.7)

        oat_group = VGroup(cup_oat_x, col_oat)
        box_oat = RoundedRectangle(
            corner_radius=0.15,
            stroke_color=YELLOW,
            stroke_width=2
        )
        box_oat.surround(oat_group).scale(1.1)

        x1_scalar = MathTex("x_1", color=YELLOW).scale(0.9)
        x1_scalar.next_to(oat_group, LEFT, buff=0.3)

        self.play(Create(box_oat), FadeIn(x1_scalar), run_time=0.8)

        # 3) Repeat for yogurt (x_2) -----------------------------------------------
        cup_yog_x = MathTex(r"x_2\ \text{cup}", color=BLUE)
        cup_yog_x.next_to(yog_name, DOWN, buff=0.12)

        self.play(ReplacementTransform(cup_yog, cup_yog_x), run_time=0.7)

        yog_group = VGroup(cup_yog_x, col_yog)
        box_yog = RoundedRectangle(
            corner_radius=0.15,
            stroke_color=BLUE,
            stroke_width=2
        )
        box_yog.surround(yog_group).scale(1.1)

        x2_scalar = MathTex("x_2", color=BLUE).scale(0.9)
        x2_scalar.next_to(yog_group, LEFT, buff=0.3)

        self.play(Create(box_yog), FadeIn(x2_scalar), run_time=0.8)

        # 3) Repeat for raspberries (x_3) -------------------------------------------
        cup_rasp_x = MathTex(r"x_3\ \text{cup}", color=RED)
        cup_rasp_x.next_to(rasp_name, DOWN, buff=0.12)

        self.play(ReplacementTransform(cup_rasp, cup_rasp_x), run_time=0.7)

        rasp_group = VGroup(cup_rasp_x, col_rasp)
        box_rasp = RoundedRectangle(
            corner_radius=0.15,
            stroke_color=RED,
            stroke_width=2
        )
        box_rasp.surround(rasp_group).scale(1.1)

        x3_scalar = MathTex("x_3", color=RED).scale(0.9)
        x3_scalar.next_to(rasp_group, LEFT, buff=0.3)

        self.play(Create(box_rasp), FadeIn(x3_scalar), run_time=0.8)

        # 4) Plus signs and equality with question mark ----------------------------
        plus1 = MathTex("+").scale(1.3)
        plus1.next_to(box_oat, RIGHT, buff=0.4)
        plus1.align_to(box_oat, DOWN)

        plus2 = MathTex("+").scale(1.3)
        plus2.next_to(box_yog, RIGHT, buff=0.4)
        plus2.align_to(box_yog, DOWN)

        eq = MathTex("=").scale(1.3)
        eq.next_to(box_rasp, RIGHT, buff=0.6)
        eq.align_to(box_rasp, DOWN)

        qmark = MathTex("?").scale(1.0)
        qmark.next_to(eq, UP, buff=0.1)

        tgt_group = VGroup(tgt_label, tgt_col)
        box_tgt = RoundedRectangle(
            corner_radius=0.15,
            stroke_color=PURPLE,
            stroke_width=2
        )
        box_tgt.surround(tgt_group, buffer=0.25)

        self.play(
            FadeIn(plus1),
            FadeIn(plus2),
            FadeIn(eq),
            Create(box_tgt),
            FadeIn(qmark),
            run_time=1.0
        )
        if DEV_MODE:
            self.interactive_embed()

