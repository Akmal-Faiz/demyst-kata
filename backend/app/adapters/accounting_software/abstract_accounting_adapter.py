from abc import ABC, abstractmethod

class AbstractAccountingAdapter(ABC):
    @abstractmethod
    def fetch_balance_sheet(self, business_name, business_year_established):
        pass
    
    @abstractmethod
    def normalize_balance_sheet(self, balance_sheet):
        pass