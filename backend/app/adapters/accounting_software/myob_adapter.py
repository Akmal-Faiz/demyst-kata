from .abstract_accounting_adapter import AbstractAccountingAdapter


class MYOBAdapter(AbstractAccountingAdapter):
    name = "MYOB"

    def fetch_balance_sheet(self, business_name, business_year_established):
        balance_sheet = [
            {
                "year": 2023,
                "month": 4,
                "monthlyProfit": 100000,
                "assetsValue": 150000
            },
            {
                "year": 2023,
                "month": 3,
                "monthlyProfit": 75000,
                "assetsValue": 135000
            },
            {
                "year": 2023,
                "month": 2,
                "monthlyProfit": 50000,
                "assetsValue": 120000
            },
            {
                "year": 2023,
                "month": 1,
                "monthlyProfit": 25000,
                "assetsValue": 105000
            },
            {
                "year": 2022,
                "month": 12,
                "monthlyProfit": 100000,
                "assetsValue": 100000
            },
            {
                "year": 2022,
                "month": 11,
                "monthlyProfit": 75000,
                "assetsValue": 85000
            },
            {
                "year": 2022,
                "month": 10,
                "monthlyProfit": 50000,
                "assetsValue": 70000
            },
            {
                "year": 2022,
                "month": 9,
                "monthlyProfit": 25000,
                "assetsValue": 55000
            },
            {
                "year": 2022,
                "month": 8,
                "monthlyProfit": 100000,
                "assetsValue": 40000
            },
            {
                "year": 2022,
                "month": 7,
                "monthlyProfit": 75000,
                "assetsValue": 25000
            },
            {
                "year": 2022,
                "month": 6,
                "monthlyProfit": 50000,
                "assetsValue": 10000
            },
            {
                "year": 2022,
                "month": 5,
                "monthlyProfit": 25000,
                "assetsValue": 0
            },
            {
                "year": 2022,
                "month": 4,
                "monthlyProfit": 100000,
                "assetsValue": 150000
            },
            {
                "year": 2022,
                "month": 3,
                "monthlyProfit": 75000,
                "assetsValue": 135000
            },
            {
                "year": 2022,
                "month": 2,
                "monthlyProfit": 50000,
                "assetsValue": 120000
            },
            {
                "year": 2022,
                "month": 1,
                "monthlyProfit": 25000,
                "assetsValue": 105000
            },
            {
                "year": 2021,
                "month": 12,
                "monthlyProfit": 100000,
                "assetsValue": 10000
            },
            {
                "year": 2021,
                "month": 11,
                "monthlyProfit": 75000,
                "assetsValue": 5000
            },
            {
                "year": 2021,
                "month": 10,
                "monthlyProfit": 50000,
                "assetsValue": 0
            },
            {
                "year": 2021,
                "month": 9,
                "monthlyProfit": 25000,
                "assetsValue": -5000
            },
            {
                "year": 2021,
                "month": 8,
                "monthlyProfit": 100000,
                "assetsValue": -10000
            },
            {
                "year": 2021,
                "month": 7,
                "monthlyProfit": 75000,
                "assetsValue": -15000
            },
            {
                "year": 2021,
                "month": 6,
                "monthlyProfit": 50000,
                "assetsValue": -20000
            },
            {
                "year": 2021,
                "month": 4,
                "monthlyProfit": 50000,
                "assetsValue": -20000
            }
        ]

        return balance_sheet

    def normalize_balance_sheet(self, balance_sheet):
        for item in balance_sheet:
            item["profitOrLoss"] = item.pop("monthlyProfit")
        return balance_sheet
