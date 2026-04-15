from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_doc(self, document: str):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self, document: str):
        pass

class Fax(ABC):
    @abstractmethod
    def send_fax(self, document: str):
        pass

class SimplePrinter(Printer):
    def print_doc(self, document: str):
        print(f"Печать: {document}")

class MultiFunctionDevice(Printer, Scanner):
    def print_doc(self, document: str):
        print(f"Печать: {document}")

    def scan_doc(self, document: str):
        print(f"Сканирование: {document}")

printer = SimplePrinter()
printer.print_doc("Договор.pdf")
