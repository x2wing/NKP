from .report import create_report_csv
from .db import init_db
from .db.initial_data import fill_initial_data


if __name__ == "__main__":
    # create_report_csv() 
    # init_db()
    fill_initial_data()