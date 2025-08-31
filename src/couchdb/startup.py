import helper
from Databases import all_dbs, create_database, create_databases
import import_data

def startup():
    create_databases()
    for db in all_dbs:
        import_data.import_data(db)

if __name__ == "__main__":
    startup()

