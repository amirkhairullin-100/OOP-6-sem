class SalesReport:
    def __init__(self, data: list[dict]):
        self.data = data

    def get_total(self) -> float:
        return sum(item['amount'] for item in self.data)

class HTMLFormatter:
    def render(self, report: SalesReport) -> str:
        rows = ''.join(f"<tr><td>{d['name']}</td><td>{d['amount']}</td></tr>"
                       for d in report.data)
        return f"<table>{rows}<tr><td>Итого</td><td>{report.get_total()}</td></tr></table>"

report = SalesReport([
    {'name': 'Товар A', 'amount': 1500},
    {'name': 'Товар B', 'amount': 2300},
])

formatter = HTMLFormatter()
html_output = formatter.render(report)
print(html_output)