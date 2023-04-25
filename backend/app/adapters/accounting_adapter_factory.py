from app.adapters.accounting_software import *

class AccountingAdapterFactory:
    @staticmethod
    def create_adapter(accounting_software):
        for subclass in AbstractAccountingAdapter.__subclasses__():
            if not subclass.__dict__.get("name"):
                continue
            if subclass.name == accounting_software:
                return subclass()
        raise ValueError("No adapter available for accounting software {}".format(accounting_software))

