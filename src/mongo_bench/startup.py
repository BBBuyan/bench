from coll_types.Base import Base
from time import time
from json import loads

def import_data(type: Base):
    print(f"importing {type.name}")
    batch = []
    start = time()
    with open(f"../../data/{type.name}.json", "r") as f:
        counter = 0
        iteration = 0

        for line in f:
            json_data = loads(line)
            batch.append(json_data)

            if(len(batch)>=type.batch_limit):
                type.coll.insert_many(batch)
                batch.clear()
                iteration +=1
                if iteration >= 250:
                    counter += iteration
                    iteration = 0
                    print(f"{counter}k, {time()-start:.0f}s")

        if batch:
            type.coll.insert_many(batch)

    end = time()
    print(f"took {end - start:.0f} s")

