from .decision_engine_dto import DecisionEngineDTO
import os
import yaml 
with open(os.environ["CONFIG_PATH"]) as f:
    config = yaml.safe_load(f)

class DecisionEngineAdapter:
    def __init__(self):
        self.url = config['decision-engine']['decision-engine-url']
        
    def get_decision(self, input:DecisionEngineDTO):
        return input.preAssessment_value