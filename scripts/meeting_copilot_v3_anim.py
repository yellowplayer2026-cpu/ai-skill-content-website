from manim import *

class MeetingCopilotV3(Scene):
    def construct(self):
        # 視覺風格：深夜藍灰底，設定 9:16 比例
        self.camera.background_color = "#1e2a38"
        
        # 1. 標題 (放大字體)
        title = Text("會議副駕：決策矩陣", font_size=40, color=WHITE).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # 2. 矩陣設計：手動 VGroup 排列，確保字體放大且不重疊
        # 表頭 (增加 buff 以免重疊)
        header = VGroup(
            Text("決策", font_size=28, color=WHITE),
            Text("負責人", font_size=28, color=WHITE),
            Text("期限", font_size=28, color=WHITE)
        ).arrange(RIGHT, buff=1.2).shift(UP*0.5)
        
        # 表格內容
        row = VGroup(
            Text("產出內訓教案", font_size=26, color="#2ecc71"),
            Text("Roger", font_size=26, color="#3498db"),
            Text("本週五", font_size=26, color="#f1c40f")
        ).arrange(RIGHT, buff=1.2).next_to(header, DOWN, buff=1.5)
        
        # 強化的邊框設計
        frame = SurroundingRectangle(VGroup(header, row), color="#1f4ed8", buff=0.5, fill_opacity=0.1)
        
        self.play(Create(frame), Write(header))
        self.play(Write(row))
        
        # 3. KPI 預測 (放大、高對比)
        kpi = Text("KPI 達成預測: 98%", font_size=32, color="#f1c40f").next_to(frame, DOWN, buff=0.8)
        self.play(FadeIn(kpi), Indicate(kpi))
        
        self.wait(2)
