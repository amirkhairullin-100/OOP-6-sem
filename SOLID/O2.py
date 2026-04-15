import json
import csv
import io
from abc import ABC, abstractmethod

class DataExportStrategy(ABC):
    @abstractmethod
    def export(self, data: list[dict]) -> str:
        pass

class JsonExporter(DataExportStrategy):
    def export(self, data: list[dict]) -> str:
        return json.dumps(data, ensure_ascii=False)

class CsvExporter(DataExportStrategy):
    def export(self, data: list[dict]) -> str:
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        return output.getvalue()

class DataExporter:
    def __init__(self, strategy: DataExportStrategy):
        self.strategy = strategy

    def export(self, data: list[dict]) -> str:
        return self.strategy.export(data)

records = [{'name': 'Анна', 'age': 30}, {'name': 'Иван', 'age': 25}]
json_exporter = DataExporter(JsonExporter())
csv_exporter = DataExporter(CsvExporter())

print(json_exporter.export(records))  
print(csv_exporter.export(records))   
import xml.etree.ElementTree as ET

class XmlExporter(DataExportStrategy):
    def export(self, data: list[dict]) -> str:
        root = ET.Element('records')
        for item in data:
            record = ET.SubElement(root, 'record')
            for key, value in item.items():
                child = ET.SubElement(record, key)
                child.text = str(value)
        return ET.tostring(root, encoding='unicode')

xml_exporter = DataExporter(XmlExporter())
print(xml_exporter.export(records))  