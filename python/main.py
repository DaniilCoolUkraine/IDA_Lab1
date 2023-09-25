from utils.loader import Loader
from data_processing import execute_tasks_2
from utils.csv_reader import CSV_Reader

# 2.1 load the data from Internet
load = False
if load:
    print("2.1 Load the data from Internet to nba.csv file")
    loader = Loader()
    loader.sendGetRequest()

reader = CSV_Reader()
execute_tasks_2(reader)
