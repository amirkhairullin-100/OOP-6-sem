from abc import ABC, abstractmethod

class Header(ABC):
    @abstractmethod
    def render(self, title: str, subtitle: str) -> str:
        pass

class Table(ABC):
    @abstractmethod
    def render(self, headers: list[str], rows: list[list]) -> str:
        pass

class Footer(ABC):
    @abstractmethod
    def render(self, text: str, page: int) -> str:
        pass

class PdfHeader(Header):
    def render(self, title: str, subtitle: str) -> str:
        return f"PDF Header: {title} | {subtitle}\n"

class PdfTable(Table):
    def render(self, headers: list[str], rows: list[list]) -> str:
        table_str = "PDF Table:\n" + ' | '.join(headers) + "\n"
        for row in rows:
            table_str += ' | '.join(str(item) for item in row) + "\n"
        return table_str

class PdfFooter(Footer):
    def render(self, text: str, page: int) -> str:
        return f"PDF Footer: {text} | Страница {page}\n"

class DocxHeader(Header):
    def render(self, title: str, subtitle: str) -> str:
        return f"DOCX Header: {title} - {subtitle}\n"

class DocxTable(Table):
    def render(self, headers: list[str], rows: list[list]) -> str:
        table_str = "DOCX Table:\n" + ' || '.join(headers) + "\n"
        for row in rows:
            table_str += ' || '.join(str(item) for item in row) + "\n"
        return table_str

class DocxFooter(Footer):
    def render(self, text: str, page: int) -> str:
        return f"DOCX Footer: {text} (Page {page})\n"

class DocumentFactory(ABC):
    @abstractmethod
    def create_header(self) -> Header:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

    @abstractmethod
    def create_footer(self) -> Footer:
        pass

class PdfFactory(DocumentFactory):
    def create_header(self) -> Header:
        return PdfHeader()

    def create_table(self) -> Table:
        return PdfTable()

    def create_footer(self) -> Footer:
        return PdfFooter()

class DocxFactory(DocumentFactory):
    def create_header(self) -> Header:
        return DocxHeader()

    def create_table(self) -> Table:
        return DocxTable()

    def create_footer(self) -> Footer:
        return DocxFooter()

def build_sales_report(factory: DocumentFactory, data: list[list]) -> str:
    header = factory.create_header()
    table = factory.create_table()
    footer = factory.create_footer()

    report = ""
    report += header.render("Отчёт о продажах", "Квартал 1, 2025")
    report += table.render(["Продукт", "Количество", "Сумма"], data)
    report += footer.render("Конфиденциально", 1)
    return report

if __name__ == "__main__":
   
    pdf_factory = PdfFactory()
    print(build_sales_report(pdf_factory, [["Товар А", 10, "$1000"], ["Товар Б", 5, "$500"]]))

    docx_factory = DocxFactory()
    print(build_sales_report(docx_factory, [["Товар А", 10, "$1000"], ["Товар Б", 5, "$500"]]))