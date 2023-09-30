from python.utils.loader import Loader
from data_processing import execute_task_block_2
from utils.csv_reader import CSV_Reader
from defs import get_path

# 2.1 load the data from Internet
print("2.1 Load the data from Internet to nba.csv file if not exists\n")
file_path = get_path()
Loader.send_get_request(file_path)

reader = CSV_Reader(file_path, 'nba.csv')
execute_task_block_2(reader)
