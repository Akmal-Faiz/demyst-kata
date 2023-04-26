from .abstract_strategy import AbstractStrategy

class SequentialStrategy(AbstractStrategy):
    name = "sequential"
    def apply(self, values: list[tuple[bool, int]], *args, **kwargs):
        return values[-1][1]