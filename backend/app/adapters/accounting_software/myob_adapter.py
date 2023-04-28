from .abstract_accounting_adapter import AbstractAccountingAdapter

class MYOBAdapter(AbstractAccountingAdapter):
    name="MYOB"
    
    def fetch_balance_sheet(self, business_name, business_year_established):
        balance_sheet = [
            {
                "year": 2020,
                "month": 12,
                "monthlyProfit": 0,
                "assetsValue": 0
            },
            {
                "year": 2020,
                "month": 11,
                "monthlyProfit": 0,
                "assetsValue": 0
            },
            {
                "year": 2020,
                "month": 10,
                "monthlyProfit": 0,
                "assetsValue": 0
            },
            {
                "year": 2020,
                "month": 9,
                "monthlyProfit": 0,
                "assetsValue": 0
            }
        ]
        
        return balance_sheet
    
    def normalize_balance_sheet(self, balance_sheet):
        for item in balance_sheet:
            item["profitOrLoss"] = item.pop("monthlyProfit")
        return balance_sheet
    