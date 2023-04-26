from .abstract_strategy import AbstractStrategy

class AggressiveStrategy(AbstractStrategy):
    name = "aggressive"
    def apply(self, values: list[tuple[bool, int]]):
        return max([v[1] for v in values])