from Databases import all_dbs
import database_operations as db_ops

def startup():
    db_ops.create_databases()
    for db in all_dbs:
        db_ops.import_docs(db)

if __name__ == "__main__":
    startup()
