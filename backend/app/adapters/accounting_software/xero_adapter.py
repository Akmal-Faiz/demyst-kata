from app.adapters.accounting_software import AbstractAccountingAdapter

class XeroAdapter(AbstractAccountingAdapter):
    name="Xero"
    
    def fetch_balance_sheet(self, business_name, business_year_established):
        balance_sheet = [
            {
                "year": 2020,
                "month": 12,
                "profitOrLoss": 250000,
                "assetsValue": 1234
            },
            {
                "year": 2020,
                "month": 11,
                "profitOrLoss": 1150,
                "assetsValue": 5789
            },
            {
                "year": 2020,
                "month": 10,
                "profitOrLoss": 2500,
                "assetsValue": 22345
            },
            {
                "year": 2020,
                "month": 9,
                "profitOrLoss": -187000,
                "assetsValue": 223452
            },
            {
                "year": 2020,
                "month": 8,
                "profitOrLoss": 250000,
                "assetsValue": 1234
            },
            {
                "year": 2020,
                "month": 7,
                "profitOrLoss": 1150,
                "assetsValue": 5789
            },
            {
                "year": 2020,
                "month": 6,
                "profitOrLoss": 2500,
                "assetsValue": 22345
            },
            {
                "year": 2020,
                "month": 5,
                "profitOrLoss": -187000,
                "assetsValue": 223452
            },
            {
                "year": 2020,
                "month": 4,
                "profitOrLoss": 250000,
                "assetsValue": 1234
            },
            {
                "year": 2020,
                "month": 3,
                "profitOrLoss": 1150,
                "assetsValue": 5789
            },
            {
                "year": 2020,
                "month": 2,
                "profitOrLoss": 2500,
                "assetsValue": 22345
            },
            {
                "year": 2020,
                "month": 1,
                "profitOrLoss": -187000,
                "assetsValue": 223452
            }
        ]
        
        return balance_sheet
    
    def normalize_balance_sheet(self, balance_sheet):
        return balance_sheet