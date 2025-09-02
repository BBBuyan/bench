from Base import Base
from Databases import obj_list, flat_list
import helper


def run():
    for db in obj_list:
        helper.create_analytic_views(db)

if __name__ == "__main__":
    run()
