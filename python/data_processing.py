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

    print("2.6 Rename columns 'seasongame' to 'season_game' and 'pts' to 'points'")
    reader.rename_column("seasongame", "season_game")
    reader.rename_column("pts", "points")
    print(reader.get_dataset_head(), end='\n\n')
