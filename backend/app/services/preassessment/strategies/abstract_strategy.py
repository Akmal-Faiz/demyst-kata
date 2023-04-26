from abc import ABC, abstractmethod

class AbstractStrategy(ABC):
    @abstractmethod
    def apply(self, values: list[tuple[bool, int]], *args, **kwargs):
        pass