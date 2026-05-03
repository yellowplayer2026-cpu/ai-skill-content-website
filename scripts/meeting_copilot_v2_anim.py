from manim import *

class MeetingCopilotV2(Scene):
    def construct(self):
        # 視覺風格：深夜藍灰底，設定 9:16 比例
        self.camera.background_color = "#1e2a38"
        
        # 1. 標題
        title = Text("會議副駕：決策矩陣自動化", font_size=32, color=WHITE).to_edge(UP)
        self.play(Write(title))

        # 2. 會議雜訊
        noise = VGroup(*[Text("討論...", font_size=18, color=GRAY) for _ in range(8)])
        noise.arrange_in_grid(4, 2, buff=0.5).shift(UP*0.5)
        self.play(FadeIn(noise))

        # 3. 決策矩陣框架
        # 使用 Matrix 概念呈現
        matrix = Table(
            [["...", "...", "..."]],
            col_labels=[Text("決策", font_size=16), Text("負責人", font_size=16), Text("期限", font_size=16)],
            include_outer_lines=True
        ).scale(0.6).shift(DOWN*0.5)
        
        self.play(Create(matrix))
        
        # 4. AI 轉換效果：文字被吸入矩陣
        self.play(noise.animate.move_to(matrix.get_center()).fade(1))
        
        # 5. 填入內容
        decision = Text("產出內訓教案", font_size=18, color="#2ecc71").move_to(matrix.get_cell((2, 1)).get_center())
        owner = Text("Roger", font_size=18, color="#1f4ed8").move_to(matrix.get_cell((2, 2)).get_center())
        deadline = Text("本週五", font_size=18, color="#e67e22").move_to(matrix.get_cell((2, 3)).get_center())
        
        self.play(Write(decision), Write(owner), Write(deadline))
        
        # 6. KPI 達成
        kpi = Text("KPI 達成預測: 98%", font_size=24, color="#f1c40f").next_to(matrix, DOWN, buff=0.5)
        self.play(FadeIn(kpi))
        self.play(Indicate(kpi))
        self.wait(2)
