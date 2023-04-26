from app.services.preassessment.rules import *

class RuleFactory:
    @staticmethod
    def create_rule(rule_name):
        for subclass in AbstractRule.__subclasses__():
            if not subclass.__dict__.get("name"):
                continue
            if subclass.name == rule_name:
                return subclass()
        raise ValueError("Rule {} was not implemented".format(rule_name))

