from app.services.preassessment.strategies import AggressiveStrategy
from .strategy_test_data import *

def test_aggressive_strategy():
    strategy = AggressiveStrategy()
    values = VALUES_1
    assert strategy.apply(values) == 100