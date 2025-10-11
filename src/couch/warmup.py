from . import operations as op
from src.couch.db_types.Base import Base

def read_warmup(type: Base):
    for _ in range(3):
        t = op.time_read(type)
        print(f"{round(t)}, ", end="", flush=True)
