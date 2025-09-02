from Base import Base
from Databases import obj_list, flat_list, arr_list
import helper


def run():
    for db in arr_list:
        helper.create_analytic_views(db)

if __name__ == "__main__":
    run()
