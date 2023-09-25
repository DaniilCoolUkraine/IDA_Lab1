from utils.loader import Loader
from utils.csv_reader import CSV_Reader
from data_processing import execute_tasks

print()

loader = Loader()
loader.sendGetRequest()

reader = CSV_Reader()

print(reader.get_data_count())
print(reader.get_table_shape())

print()
print(reader.get_types())

print()
if reader.has_null():
	print(f"all nulls count: {reader.get_nulls_count()}")
else:
	print("data is full")

column = "game_id"

if reader.column_has_null(column):
	print(f"{column} nulls count: {reader.get_nulls_count_in_column(column)}")
else:
	print(f"{column} data is full")

column = "notes"

if reader.column_has_null(column):
	print(f"{column} nulls count: {reader.get_nulls_count_in_column(column)}")
else:
	print(f"{column} data is full")

print()
reader.delete_column(column)
print(f"all nulls count: {reader.get_nulls_count()}")

execute_tasks()
