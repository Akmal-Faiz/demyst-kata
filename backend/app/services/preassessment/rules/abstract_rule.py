from abc import ABC, abstractmethod

class AbstractRule(ABC):
    @abstractmethod
    def evaluate(self, *args, **kwargs) -> tuple[bool, int]:
        pass
