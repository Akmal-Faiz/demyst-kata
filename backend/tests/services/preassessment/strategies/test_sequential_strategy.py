from app.services.preassessment.strategies import SequentialStrategy
from .strategy_test_data import *

def test_sequential_strategy():
    strategy = SequentialStrategy()
    values = VALUES_1
    assert strategy.apply(values) == 60