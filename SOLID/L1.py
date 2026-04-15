from abc import ABC, abstractmethod
from typing import List

class Bird(ABC):
    pass

class Flyer(ABC):
    @abstractmethod
    def fly(self) -> str:
        ...

class Sparrow(Bird, Flyer):
    def fly(self) -> str:
        return "Воробей летит"

class Penguin(Bird):
    pass

def make_birds_fly(birds: List[Bird]) -> None:
    for bird in birds:
        if isinstance(bird, Flyer):
            print(bird.fly())
        else:
            print(f"{bird.__class__.__name__} не умеет летать")

birds: List[Bird] = [Sparrow(), Penguin()]
make_birds_fly(birds)