import yaml
import os
from enum import Enum

class ACCOUNTING_SOFTWARE(str, Enum):
    pass

with open(os.environ["CONFIG_PATH"]) as f:
    config = yaml.safe_load(f)

acc_software_list = list(config['accounting-software'].keys())

ACCOUNTING_SOFTWARE = Enum("ACCOUNTING_SOFTWARE", {value: value for value in acc_software_list})

