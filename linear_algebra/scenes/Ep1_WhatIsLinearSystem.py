from manim import *
from manim.opengl import *

DEV_MODE = True  # set to False for final video

BG ="#080818"\

# Per cup vectors (cal, protein, sugar)
OAT_VEC  = [120, 3, 7]
YOG_VEC  = [90, 21, 1]
RASP_VEC = [64, 1, 5]
TGT_VEC  = [394, 28, 24]

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

        # Fade out title, show question, highlight target column---------------------
        question = Text(
            "Can the ingredients be scaled to match the target?",
            font_size=26
        ).to_edge(UP)

        self.play(FadeOut(title, run_time=0.5))
        self.play(FadeIn(question, shift=UP, run_time=0.8))

        box_oat = RoundedRectangle(
                    corner_radius=0.15,
                    width=col_oat.width * 1.2,   # padding factor
                    height=col_oat.height * 1.2, # padding factor
                    stroke_color=YELLOW,
                    stroke_width=2
                )
        box_oat.move_to(col_oat.get_center())


        box_yog = RoundedRectangle(
            corner_radius=0.15,
            width=box_oat.width,   # padding factor
            height=col_yog.height * 1.2, # padding factor
            stroke_color=BLUE,
            stroke_width=2
        )
        box_yog.move_to(col_yog.get_center())

        
        box_rasp = RoundedRectangle(
            corner_radius=0.15,
            width=box_oat.width,   # padding factor
            height=col_rasp.height * 1.2, # padding factor
            stroke_color=RED,
            stroke_width=2
        )
        box_rasp.move_to(col_rasp.get_center())

        block_oat = VGroup(box_oat, col_oat)
        block_yog = VGroup(box_yog, col_yog)
        block_rasp = VGroup(box_rasp, col_rasp)

        self.play(
            Indicate(
                VGroup(block_oat, block_yog, block_rasp),
                scale_factor=1.05
            ),
            run_time=1.0
        )

        #--------------------------------------------------------------------------
        self.play(
            Indicate(
                VGroup(tgt_label, tgt_col),
                color=PURPLE,
                scale_factor=1.05
            ),
            run_time=1.0
        )

        # Change "1 cup" -> "x_1 cup", add rounded rectangle and x_1--------------
        cup_oat_x = MathTex(r"x_1\ \text{cup}", color=YELLOW, font_size=30)
        cup_oat_x.next_to(oat_name, DOWN, buff=0.12)

        self.play(ReplacementTransform(cup_oat, cup_oat_x), run_time=0.7)

        x1_scalar = MathTex("x_1", color=YELLOW).scale(0.9)
        x1_scalar.next_to(col_oat, LEFT, buff=0.3)

        self.play(FadeIn(x1_scalar), run_time=0.8)

        # Repeat for yogurt (x_2) -----------------------------------------------
        cup_yog_x = MathTex(r"x_2\ \text{cup}", color=BLUE, font_size=30)
        cup_yog_x.next_to(yog_name, DOWN, buff=0.12)

        self.play(ReplacementTransform(cup_yog, cup_yog_x), run_time=0.7)

        x2_scalar = MathTex("x_2", color=BLUE).scale(0.9)
        x2_scalar.next_to(col_yog, LEFT, buff=0.3)

        self.play(FadeIn(x2_scalar), run_time=0.8)
    

        #Repeat for raspberries (x_3) -------------------------------------------
        cup_rasp_x = MathTex(r"x_3\ \text{cup}", color=RED, font_size=30)
        cup_rasp_x.next_to(rasp_name, DOWN, buff=0.12)

        self.play(ReplacementTransform(cup_rasp, cup_rasp_x), run_time=0.7)

        x3_scalar = MathTex("x_3", color=RED).scale(0.9)
        x3_scalar.next_to(col_rasp, LEFT, buff=0.3)

        self.play(FadeIn(x3_scalar), run_time=0.8)

        # Plus signs and equality with question mark ----------------------------
        plus1 = MathTex("+").scale(1.1)
        plus1.next_to(x2_scalar, LEFT, buff=0.2)

        plus2 = MathTex("+").scale(1.1)
        plus2.next_to(x3_scalar, LEFT, buff=0.3)

        eq = MathTex("=").scale(1.1)
        eq.next_to(box_rasp, RIGHT, buff=0.6)

        qmark = MathTex("?").scale(1.0)
        qmark.next_to(eq, UP, buff=0.1)

        self.play(
            FadeIn(plus1),
            FadeIn(plus2),
            FadeIn(eq),
            FadeIn(qmark)
        )

        self.play(Indicate(tgt_col, color=PURPLE), run_time=1.0)

        # Transition to row picture ----------------------------------------------

        # ------------------------------------------------------------------
        # 1) Fade out column boxes, distribute x_i scalars to each entry
        # ------------------------------------------------------------------

        # Fade out the column highlight boxes
        self.play(
            FadeOut(box_oat),
            FadeOut(box_yog),
            FadeOut(box_rasp)
        )

        # --- x1 distributed to the right of each oat entry ---
        x1_row_factors = VGroup()
        for entry in col_oat:
            x1_copy = x1_scalar.copy().scale(0.8)
            x1_copy.next_to(entry, RIGHT, buff=0.12)
            x1_row_factors.add(x1_copy)

        # Align all x1 copies under each other (vertical alignment)
        x1_row_factors.arrange(DOWN, buff=0.45)
        x1_row_factors.move_to(col_oat.get_right() + RIGHT * 0.3)

        self.play(
            *[TransformFromCopy(x1_scalar, x1_copy) for x1_copy in x1_row_factors],
            FadeOut(x1_scalar),
            run_time=1.0
        )

        # --- x2 distributed to the right of each yog entry ---
        x2_row_factors = VGroup()
        for entry in col_yog:
            x2_copy = x2_scalar.copy().scale(0.8)
            x2_copy.next_to(entry, RIGHT, buff=0.12)
            x2_row_factors.add(x2_copy)

        x2_row_factors.arrange(DOWN, buff=0.45)
        x2_row_factors.move_to(col_yog.get_right() + RIGHT * 0.3)

        self.play(
            *[TransformFromCopy(x2_scalar, x2_copy) for x2_copy in x2_row_factors],
            FadeOut(x2_scalar),
            run_time=1.0
        )


        # --- x3 distributed to the right of each rasp entry ---
        x3_row_factors = VGroup()
        for entry in col_rasp:
            x3_copy = x3_scalar.copy().scale(0.8)
            x3_copy.next_to(entry, RIGHT, buff=0.12)
            x3_row_factors.add(x3_copy)

        x3_row_factors.arrange(DOWN, buff=0.45)
        x3_row_factors.move_to(col_rasp.get_right() + RIGHT * 0.3)

        self.play(
            *[TransformFromCopy(x3_scalar, x3_copy) for x3_copy in x3_row_factors],
            FadeOut(x3_scalar),
            run_time=1.0
        )

        # ------------------------------------------------------------------
        # 2) Duplicate plus signs and equality into row-wise versions,
        #    aligned with the new x_i copies and target entries
        # ------------------------------------------------------------------

        plus1_row_copies = VGroup()
        plus2_row_copies = VGroup()
        eq_row_copies    = VGroup()

        for i in range(3):
            # + between the x1-row term and x2-row term (cal/protein/sugar rows)
            p1 = plus1.copy().scale(0.9)
            p1.next_to(x1_row_factors[i], RIGHT, buff=0.12)
            plus1_row_copies.add(p1)

            # + between the x2-row term and x3-row term
            p2 = plus2.copy().scale(0.9)
            p2.next_to(x2_row_factors[i], RIGHT, buff=0.12)
            plus2_row_copies.add(p2)

            # = just before the target entry in that row
            e = eq.copy().scale(0.9)
            e.next_to(tgt_col[i], LEFT, buff=0.15)
            eq_row_copies.add(e)

        # Animate the single-line +, +, = "splitting" into row-wise copies
        self.play(
            *[TransformFromCopy(plus1, p) for p in plus1_row_copies],
            *[TransformFromCopy(plus2, p) for p in plus2_row_copies],
            *[TransformFromCopy(eq,   e) for e in eq_row_copies],
            FadeOut(plus1),
            FadeOut(plus2),
            FadeOut(eq),
            FadeOut(qmark),
            run_time=1.3
        )
        if DEV_MODE:
            self.interactive_embed()

        

