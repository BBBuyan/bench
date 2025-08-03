import pymongo
from pprint import pprint
from flat_helpers import create_index, delete_indexes
import flat_workloads as workload

cl = pymongo.MongoClient("mongodb://192.168.2.87:27017")

db = cl["deep"]
col = db["flat"]

workload.run_read_heavy(col)
workload.run_analytic(col)
workload.run_insert_heavy(col)
workload.run_update_heavy(col)
workload.run_mixed(col)
print("-------------")

create_index(col)
workload.run_read_heavy(col)
workload.run_analytic(col)
workload.run_insert_heavy(col)
workload.run_update_heavy(col)
workload.run_mixed(col)
delete_indexes(col)
