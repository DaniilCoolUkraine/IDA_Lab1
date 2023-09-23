import pandas as pd

class CSV_Reader:
	def __init__(self) -> None:
		self.nba = pd.read_csv("python/dataset/nba.csv")
	
	def get_data_count(self):
		return len(self.nba)
	def get_table_shape(self):
		return self.nba.shape
	
	def get_types(self):
		return self.nba.dtypes
	
	def has_null(self):
		return self.get_nulls_count() != 0
	def get_nulls_count(self):
		return self.nba.isnull().sum().sum()
	
	def column_has_null(self, column):
		return self.get_nulls_count_in_column(column) != 0
	def get_nulls_count_in_column(self, column):
		return self.nba[column].isnull().sum()
	
	def delete_column(self, column):
		self.nba = self.nba.drop([column], axis=1)