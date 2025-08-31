import operations as op
from Base import Base

def warmup_insert(types: list[Base]):
    for type in types:
        op.time_insert(type)

def warmup_update(types: list[Base]):
    for type in types:
        op.time_update(type)
