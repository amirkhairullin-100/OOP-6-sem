from abc import ABC, abstractmethod
from typing import List

class SortAlgorithm(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        ...

class BubbleSort(SortAlgorithm):
    def sort(self, data: List[int]) -> List[int]:
        arr = data[:]
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class BuiltinSort(SortAlgorithm):
    def sort(self, data: List[int]) -> List[int]:
        return sorted(data)

class Sorter:
    def __init__(self, algorithm_factory):
        """
        algorithm_factory: функция без параметров, возвращающая экземпляр SortAlgorithm
        """
        self.algorithm_factory = algorithm_factory

    def sort(self, data: List[int]) -> List[int]:
        algo = self.algorithm_factory()
        return algo.sort(data)

numbers = [5, 3, 8, 1, 9, 2]

sorter_bubble = Sorter(lambda: BubbleSort())
print(sorter_bubble.sort(numbers))

sorter_builtin = Sorter(lambda: BuiltinSort())
print(sorter_builtin.sort(numbers))