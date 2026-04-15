from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker, Eater):
    def work(self):
        print("Человек работает")
    def eat(self):
        print("Человек обедает")

class RobotWorker(Worker):
    def work(self):
        print("Робот работает")

def manage(workers: list[Worker]):
    for w in workers:
        w.work()

def manage_eaters(workers: list[Worker], eaters: list[Eater]):
    for w in workers:
        w.work()
    for e in eaters:
        e.eat()

human = HumanWorker()
robot = RobotWorker()

manage([human])  
manage([robot])  

print("---")

manage_eaters([human], [human])  