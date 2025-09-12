from src.base_types import Base
from .es_operations import time_read
from src.all_types import arr_types

Base.is_debug = True
print(time_read(arr_types[0]))

