from manim import *

class ContentPipeline(Scene):
    def construct(self):
        # 視覺風格：深夜藍灰底，設定 9:16 比例
        self.camera.background_color = "#1e2a38"
        
        # 標題
        title = Text("AI-SG 內容治理架構", font_size=36, color=WHITE).to_edge(UP)
        self.play(Write(title))

        # 1. 傳統備課區 (Y軸：時間流，臃腫)
        traditional = Text("傳統備課 (臃腫)", font_size=24, color="#e74c3c").shift(LEFT*1.5 + UP*1)
        blocks = VGroup(*[Square(side_length=0.4, color="#e74c3c", fill_opacity=0.6) for _ in range(6)])
        blocks.arrange(DOWN, buff=0.1).next_to(traditional, DOWN)
        
        self.play(Create(traditional), Create(blocks))
        self.wait(1)

        # 2. AI 漏斗 (AEDDI 模型)
        funnel = Polygon(LEFT*1.2+UP*1, RIGHT*1.2+UP*1, ORIGIN, color="#f1c40f", fill_opacity=0.3)
        funnel_text = Text("AEDDI 評估漏斗", font_size=20, color="#f1c40f").next_to(funnel, UP)
        
        self.play(FadeIn(funnel), Write(funnel_text))
        self.play(blocks.animate.shift(RIGHT*1.5 + DOWN*1.5).scale(0.5))
        self.wait(1)

        # 3. 價值飛躍 (Z軸：價值流)
        result = Text("高客單教案 (精煉)", font_size=24, color="#2ecc71").shift(RIGHT*1.5 + UP*1)
        z_arrow = Arrow(start=ORIGIN, end=UP*2, color="#2ecc71").next_to(result, DOWN)
        
        self.play(Create(result), GrowArrow(z_arrow))
        self.play(Indicate(result))
        
        # 結尾：AI 秘書長精神
        final_msg = Text("顧問轉型，從自動化開始", font_size=32, color="#1f4ed8").to_edge(DOWN)
        self.play(Write(final_msg))
        self.wait(2)
