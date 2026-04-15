from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def charge(self, amount: float):
        pass

class Refundable(ABC):
    @abstractmethod
    def refund(self, transaction_id: str):
        pass

class TransactionHistoryProvider(ABC):
    @abstractmethod
    def get_transaction_history(self) -> list:
        pass

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self) -> str:
        pass

class FullGateway(PaymentProcessor, Refundable, TransactionHistoryProvider, ReportGenerator):
    def charge(self, amount: float):
        print(f"Списание: {amount} руб.")
        
    def refund(self, transaction_id: str):
        print(f"Возврат по транзакции {transaction_id}")
        
    def get_transaction_history(self) -> list:
        return [{'id': 'tx1', 'amount': 500}]
        
    def generate_report(self) -> str:
        return "Отчёт: транзакций — 1"

class BasicGateway(PaymentProcessor):
    def charge(self, amount: float):
        print(f"Списание: {amount} руб.")

gw = BasicGateway()
gw.charge(1500.0)