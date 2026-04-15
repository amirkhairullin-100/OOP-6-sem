class PdfReport:
    def generate(self, data: dict) -> str:
        return f"[PDF] Отчёт: {data}"

class ExcelReport:
    def generate(self, data: dict) -> str:
        return f"[Excel] Отчёт: {data}"

class CsvReport:
    def generate(self, data: dict) -> str:
        return f"[CSV] Отчёт: {data}"

class ReportManager:
    def __init__(self):
        pass

    def create_report_generator(self):
        """Фабричный метод, который подклассы переопределяют"""
        raise NotImplementedError

    def export(self, data: dict) -> str:
        generator = self.create_report_generator()
        return generator.generate(data)

class PdfReportManager(ReportManager):
    def create_report_generator(self):
        return PdfReport()

class ExcelReportManager(ReportManager):
    def create_report_generator(self):
        return ExcelReport()

class CsvReportManager(ReportManager):
    def create_report_generator(self):
        return CsvReport()

manager = PdfReportManager()
print(manager.export({"title": "Продажи Q1", "total": 150000}))

manager = ExcelReportManager()
print(manager.export({"title": "Продажи Q2", "total": 250000}))

manager = CsvReportManager()
print(manager.export({"title": "Продажи Q3", "total": 350000}))