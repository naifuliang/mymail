from utils.DB_Operations.models import *

def create_table():
    if not Accounts.table_exists():
        Accounts.create_table()
    if not In_box.table_exists():
        In_box.create_table()

if __name__ == "__main__":
    create_table()