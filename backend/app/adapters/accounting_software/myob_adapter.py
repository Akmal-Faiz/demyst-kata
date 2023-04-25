from .abstract_accounting_adapter import AbstractAccountingAdapter

class MYOBAdapter(AbstractAccountingAdapter):
    name="MYOB"
    
    def fetch_balance_sheet(self, business_name, business_year_established):
        balance_sheet = [
            {
                "year": 2020,
                "month": 12,
                "monthlyProfit": 250000,
                "assetsValue": 1234
            },
            {
                "year": 2020,
                "month": 11,
                "monthlyProfit": 1150,
                "assetsValue": 5789
            },
            {
                "year": 2020,
                "month": 10,
                "monthlyProfit": 2500,
                "assetsValue": 22345
            },
            {
                "year": 2020,
                "month": 9,
                "monthlyProfit": -187000,
                "assetsValue": 223452
            }
        ]
        
        return 