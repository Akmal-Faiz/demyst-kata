from .abstract_rule import AbstractRule

class ProfitLastYearRule(AbstractRule):
    name = "profit-last-year"
    
    def evaluate(self, balance_sheet, *args, **kwargs) -> tuple[bool, int]:
        sorted_balance_sheet = sorted(
            balance_sheet, 
            key=lambda x: (x["year"], x["month"]), 
            reverse=True
            )
        if sum([m["profitOrLoss"] for m in sorted_balance_sheet[:12]]) > 0:
            return True, 60
        else:
            return False, None