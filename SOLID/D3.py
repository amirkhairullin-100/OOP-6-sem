from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render(self, content: str) -> str:
        pass

class PdfRenderer(Renderer):
    def render(self, content: str) -> str:
        return f"[PDF] {content}"

class HtmlRenderer(Renderer):
    def render(self, content: str) -> str:
        return f"<html><body>{content}</body></html>"

class ReportGenerator:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def generate(self, data: str) -> str:
        content = f"Отчёт: {data}"
        return self.renderer.render(content)

pdf_renderer = PdfRenderer()
html_renderer = HtmlRenderer()

generator_pdf = ReportGenerator(pdf_renderer)
print(generator_pdf.generate("Продажи за март"))

generator_html = ReportGenerator(html_renderer)
print(generator_html.generate("Продажи за март"))