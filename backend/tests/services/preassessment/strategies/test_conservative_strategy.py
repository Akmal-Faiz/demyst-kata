from app.services.preassessment.strategies import ConservativeStrategy
from .strategy_test_data import *

def test_conservative_strategy():
    strategy = ConservativeStrategy()
    values = VALUES_1
    assert strategy.apply(values) == 10