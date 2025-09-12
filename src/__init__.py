from dotenv import load_dotenv
from .all_types import all_types, obj_types, arr_types, flat_types
from .base_types import Base, Obj, Arr, Flat

load_dotenv()

print("main src")
__all__ = [
    "all_types"
    , "obj_types"
    , "arr_types"
    , "flat_types"
    , "Base"
    , "Flat"
    , "Arr"
    , "Obj"
]
