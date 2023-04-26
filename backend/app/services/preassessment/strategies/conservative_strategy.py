from .abstract_strategy import AbstractStrategy

class ConservativeStrategy(AbstractStrategy):
    name = "conservative"
    def apply(self, values: list[tuple[bool, int]], *args, **kwargs):
        return min([v[1] for v in values])