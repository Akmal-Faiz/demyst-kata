from .rule_factory import RuleFactory
from .strategy_factory import StrategyFactory
import os
import yaml

with open(os.environ["CONFIG_PATH"]) as f:
    config = yaml.safe_load(f)

class RuleEngine:
    def __init__(self):
        rule_names = [rule for rule in config['rule-engine']['rules'] if config['rule-engine']['rules'][rule]['active']]
        self.rules = [RuleFactory.create_rule(i) for i in rule_names]
        
        strategy_names = [strat for strat in config['rule-engine']['strategies'] if config['rule-engine']['strategies'][strat]['active']]
        if len(strategy_names) != 1:
            raise ValueError("There must be exactly 1 active strategy. Please reconfigure the config.yml file.")
        self.strategy = StrategyFactory.create_strategy(strategy_names[0]) 
        
        self.default = 20

    def evaluate(self, *args, **kwargs):
        values = []
        for rule in self.rules:
            rule_result = rule.evaluate(*args)
            if rule_result[0]:
                values.append(rule_result)
        if not values:
            return self.default
        
        strat_result = self.strategy.apply(values)
        
        if not strat_result:
            return self.default
        else:
            return strat_result