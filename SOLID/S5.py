import csv
import io

class CsvReader:
    @staticmethod
    def read(csv_content: str):
        reader = csv.DictReader(io.StringIO(csv_content))
        return [row for row in reader]

class CsvWriter:
    @staticmethod
    def write(output_path: str, rows: list[dict]):
        if not rows:
            return
        
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

class CsvProcessor:
    def process(self, csv_content: str, output_path: str):
        reader = CsvReader()
        writer = CsvWriter()
        
        rows = reader.read(csv_content)
        writer.write(output_path, rows)
        return rows

content = "name,age\nАнна,30\nИван,25"
processor = CsvProcessor()
data = processor.process(content, "/tmp/output.csv")
for row in data:
    print(row)