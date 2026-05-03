from manim import *

class MeetingCopilot(Scene):
    def construct(self):
        # 視覺風格：深夜藍灰底，設定 9:16 比例
        self.camera.background_color = "#1e2a38"
        
        # 1. 標題
        title = Text("會議副駕：從雜訊到決策", font_size=36, color=WHITE).to_edge(UP)
        self.play(Write(title))
        
        # 2. 會議紀錄文字瀑布
        raw_text_content = ["需求討論...", "雜訊干擾...", "待辦清單...", "KPI 確認...", "決策模糊..."]
        raw_text = VGroup(*[Text(txt, font_size=20, color=GRAY) for txt in raw_text_content])
        raw_text.arrange(DOWN, buff=0.3).shift(UP*0.5)
        self.play(FadeIn(raw_text, shift=DOWN))
        
        # 3. AI 處理濾鏡 (AE-DDI 治理核心)
        filter_box = Rectangle(width=4, height=1.2, color="#1f4ed8", fill_opacity=0.3).shift(DOWN*1.5)
        filter_text = Text("AI 決策濾鏡 (Decision-Flow)", font_size=20, color="#1f4ed8").move_to(filter_box.get_center())
        self.play(Create(filter_box), Write(filter_text))
        
        # 動畫：文字掉入濾鏡
        self.play(raw_text.animate.shift(DOWN*2).set_opacity(0.2))
        
        # 4. 決策呈現 (Z軸價值流：可執行決策)
        decision = Text("✅ 決策：本週五前完成簡報", font_size=24, color="#2ecc71").next_to(filter_box, DOWN, buff=0.5)
        self.play(Write(decision))
        
        # 5. 進度條
        bar = Rectangle(width=3, height=0.2, color="#f1c40f").next_to(decision, DOWN, buff=0.3)
        bar_fill = Rectangle(width=0, height=0.2, color="#f1c40f", fill_opacity=1).align_to(bar, LEFT)
        self.play(Create(bar), FadeIn(bar_fill))
        self.play(bar_fill.animate.set_width(3), run_time=2)
        
        self.wait(1)
