import requests
import operations 
import workloads
import workloads_analytic as work_a
from pprint import pprint
import database_operations
from Base import Base
import helper
from Databases import arr_list, obj_list, flat_list

Base.debug = True
operations.time_read(obj_list[0])
