from utils.csv_reader import CSV_Reader


def execute_tasks_2(reader: CSV_Reader):
    print("print several rows of data from the table, for example")
    print(reader.get_dataset_head(), end='\n\n')

    print("2.2 print shape of DataFrame object")
    print(reader.get_table_shape(), end='\n\n')

    print("2.3 print the data types of each column")
    print(reader.get_types(), end='\n\n')

    print("2.4 Check nulls values int object")
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
        print(f"{column} nulls count after deletion: {reader.get_nulls_count_in_column(column)}")
    else:
        print(f"{column} data is full")

    print("\n2.5 Delete all unnecessary columns in table")
    reader.delete_column(column)
    print(f"all nulls count: {reader.get_nulls_count()}", end='\n\n')
    print("Checking the table after deletion (missing notes column)")
    print(reader.get_dataset_head(), end='\n\n')

    print("2.6 Rename columns 'lg_id' to 'league_id', 'pts' to 'points' and '_iscopy' to 'is_copy'")
    reader.rename_column("seasongame", "season_game")
    reader.rename_column("pts", "points")
    reader.rename_column("_iscopy", "is_copy")
    reader.rename_column("lg_id", "league_id")
    print(reader.get_dataset_head(), end='\n\n')

    print("2.7 Changing the type in the 'is_copy' column to bool type")
    reader.change_data_type("is_copy", "bool")
    print(reader.get_types(), end='\n\n')
    print(reader.get_dataset_head(), end='\n\n')

    print("2.8 Delete duplicates from table")
    old_shape = reader.get_table_shape()
    reader.delete_duplicates()

    if old_shape == reader.get_table_shape():
        print(f"There are no duplicates in the table")
    else:
        print(f"Duplicates successfully deleted")
    print("Old shape:", old_shape)
    print("Current shape:", reader.get_table_shape())

    print("2.9 Check for outliers")
    # Didn't work. Unfortunately, I do not know why :(
    '''Error: FutureWarning: is_categorical_dtype is deprecated and will be removed in a future version.
    Use isinstance(dtype, CategoricalDtype) instead if pd.api.types.is_categorical_dtype(vector): '''
    # reader.check_for_outliers_in_column("points")

    print(reader.check_for_outliers_in_column("points"), end='\n\n')
    print(reader.check_for_outliers_in_column("is_playoffs"), end='\n\n')

    print("2.10 Exclude outliers from table")


