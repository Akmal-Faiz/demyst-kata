from app.services.preassessment.strategies import *

class StrategyFactory:
    @staticmethod
    def create_strategy(strategy_name):
        for subclass in AbstractStrategy.__subclasses__():
            if not subclass.__dict__.get("name"):
                continue
            if subclass.name == strategy_name:
                return subclass()
        raise ValueError("Strategy {} was not implemented".format(strategy_name))

