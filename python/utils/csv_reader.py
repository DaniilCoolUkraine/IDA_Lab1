import pandas as pd
from sys import platform


class CSV_Reader:
	def __init__(self) -> None:
		pd.set_option("display.width", 1000)  # To avoid table migration
		if platform == 'linux':
			self.nba = pd.read_csv("dataset/nba.csv")
		else:
			self.nba = pd.read_csv("python/dataset/nba.csv")
	
	def get_data_count(self):
		return len(self.nba)

	def get_table_shape(self):
		return self.nba.shape
	
	def get_types(self):
		return self.nba.dtypes

	def get_dataset_head(self):
		pd.set_option("display.max.columns", None)
		pd.set_option("display.precision", 2)
		return self.nba.head()

	def get_dataset_statistic(self):
		return self.nba.describe()

	def get_column_values(self, column):
		return self.nba[column].value_counts()
	
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

	def rename_column(self, from_str: str, to_str: str):
		self.nba = self.nba.rename(columns={from_str: to_str})

	def change_data_type(self, column: str, to_type: str):
		self.nba[column] = self.nba[column].astype(to_type)

	def delete_duplicates(self):
		self.nba = self.nba.drop_duplicates()
