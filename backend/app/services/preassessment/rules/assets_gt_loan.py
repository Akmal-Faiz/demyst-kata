from .abstract_rule import AbstractRule

class AssetsGtLoanRule(AbstractRule):
    name = "assets-gt-loan"
    
    def evaluate(self, balance_sheet, loan_amt, *args, **kwargs) -> tuple[bool, int]:
        sorted_balance_sheet = sorted(
            balance_sheet, 
            key=lambda x: (x["year"], x["month"]), 
            reverse=True
            )
        if sum([m["assetsValue"] for m in sorted_balance_sheet[:12]])/12 > loan_amt:
            return True, 100
        else:
            return False, None