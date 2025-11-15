This lab is about data processing of csv file and how we could do a simple data processing(ex. like max temperature and joining table) from given csv file
We use class to handle both data handling and data manipulation

Class

DataLoader
Handles loading CSV files.

--__init__(self, base_path=None)
Initializes the DataLoader with a base path for data files.

    Attribute base_path: Path to the folder containing data files. Defaults to the parent directory of the current script if None.

--load_csv(self, filename)
Loads a CSV file and returns its contents as a list of dictionaries.

    Parameter filename: The CSV file name to read.

    Returns: List of dictionaries representing each row in the CSV.
    
DB
--init(self)
Initializes the DB with an empty list of tables.

Attribute:
    table: List to store table objects. Starts as an empty list.

--insert(self, table_list)
Inserts a table object into the table property.

Parameter:
    table_list: The table object to add to the database.

--search(self, table_name)
Searches for a table object by name. Returns the table if found, otherwise returns a new empty Table object with the given name.

Parameter:
    table_name: Name of the table to search for.

Returns:
    Table object: The found table or a new empty table with the given name.



Table
#Handles data manipulation for a list of dictionaries (table-like data).

__init__(self, text, table)
Initializes the Table with a text label and a list of dictionaries.

Attribute 
    text: Placeholder text (currently unused).
    table: Stores the processed list of dictionaries; numeric values are automatically converted to float.

__float_table(self, list_item)
Converts all values in the dictionary list that can be cast to float. Non-numeric values remain unchanged.

Parameter 
    list_item: List of dictionaries to process.

Returns: 
    New list of dictionaries with numeric values converted to float.

filter(self, condition=lambda x: x)
Filters the table according to a custom condition and returns a new Table object containing only matching rows.

Parameter 
    condition: A function applied to each row to determine if it should be included. Default returns all rows.

aggregate(self, aggregate_function, aggregate_key)
Runs a function on all values of a selected key in the table.

Parameter 
    aggregate_function: Function to apply (e.g., sum, max, len).
    aggregate_key: The key in each dictionary on which to run the function.

Returns: 
    Result of the aggregation function.

--join(self, input_table, joined_key)
Joins another table object with the current table object and returns a new table object containing the merged data.

Parameters:
    input_table: The table object to join with the current table.
    joined_key: The key used to match rows between the two tables.

Returns:
    Table object: A new table object containing the joined data. The name of the new table is formatted as "{self.name}_joined".


Project/
│
├── README.md                 # This file
├── Cities.csv                # The dataset
├── Countries.csv             # The dataset
└── data_processing.py        # The analysis code

How to Run and Test

1.Run the data_processing.py script.
2.Modify the lambda functions in the filter and aggregate methods to explore different queries.
3.Ensure your conditions and keys match the structure of your CSV file.