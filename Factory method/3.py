from abc import ABC, abstractmethod
import json
import csv
import io
import xml.etree.ElementTree as ET

class Parser(ABC):
    @abstractmethod
    def parse(self, raw: str) -> list[dict]:
        pass

class JsonParser(Parser):
    def parse(self, raw: str) -> list[dict]:
        return json.loads(raw)

class CsvParser(Parser):
    def parse(self, raw: str) -> list[dict]:
        return list(csv.DictReader(io.StringIO(raw)))

class XmlParser(Parser):
    def parse(self, raw: str) -> list[dict]:
        root = ET.fromstring(raw)
        return [{child.tag: child.text for child in item} for item in root]

class DataImporter(ABC):
    def parse_data(self, raw: str) -> list[dict]:
        parser = self.create_parser()
        return parser.parse(raw)
    
    @abstractmethod
    def create_parser(self) -> Parser:
        pass

class JsonImporter(DataImporter):
    def create_parser(self) -> Parser:
        return JsonParser()

class CsvImporter(DataImporter):
    def create_parser(self) -> Parser:
        return CsvParser()

class XmlImporter(DataImporter):
    def create_parser(self) -> Parser:
        return XmlParser()

json_data = '[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]'
csv_data = "name,age\nAlice,30\nBob,25"
xml_data = """
<root>
    <item><name>Alice</name><age>30</age></item>
    <item><name>Bob</name><age>25</age></item>
</root>
"""

json_importer = JsonImporter()
print(json_importer.parse_data(json_data))

csv_importer = CsvImporter()
print(csv_importer.parse_data(csv_data))

xml_importer = XmlImporter()
print(xml_importer.parse_data(xml_data))