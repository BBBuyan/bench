from src.base_types import Flat
from .import_data import get_data

fl = Flat()
i = 0
for g in get_data(fl):
    print(g)
    i+=1
    if i > 5:
        break
