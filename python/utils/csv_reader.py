import pandas as pd

# Must be involved immediately
pd.set_option("display.width", 1000)  # To avoid table migration
pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)


class CSV_Reader:
	def __init__(self, file_path: str) -> None:
		self.file_path = file_path
		self.nba = pd.read_csv(file_path + 'nba.csv')
	
	def get_data_count(self):
		return len(self.nba)

	def get_table_shape(self):
		return self.nba.shape
	
	def get_types(self):
		return self.nba.dtypes

	def get_dataset_head(self):
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

	def check_for_outliers_in_column(self, col: str):
		numeric_columns = self.nba.select_dtypes(include=['number'])
		if col not in numeric_columns:
			print("This column is not numeric")
			return

		# Calculate static characteristic for each column
		stats = numeric_columns.describe()

		# Get first and third quantiles
		q1 = stats.loc["25%", col]
		q3 = stats.loc["75%", col]

		# Calculate the interquartile range for col
		iqr = q3 - q1

		# Calculate upper and lower bounds for outliers
		lower_bound = q1 - 1.5 * iqr
		upper_bound = q3 + 1.5 * iqr
		return numeric_columns[(numeric_columns[col] < lower_bound) | (numeric_columns[col] > upper_bound)]

	def delete_outliers(self, col: str):
		outliers = self.check_for_outliers_in_column(col)

		# Delete rows with outliers
		self.nba.drop(outliers.index)
		self.nba.reset_index()

	def get_save_dir(self):
		return self.file_path

	def save_to_file(self, name: str):
		self.nba.to_csv(self.file_path + name, index=False)
