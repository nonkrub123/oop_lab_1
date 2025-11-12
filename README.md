This lab is about data processing of csv file and how we could do a simple data processing(ex. like max temperature) from given csv file
We use class to handle both data handling and data manipulation

DataLoader Class:
-Handles loading CSV files.

--__init__(self, base_path=None)
Initializes the DataLoader with a base path for data files.

    Attribute base_path: Path to the folder containing data files. Defaults to the parent directory of the current script if None.

--load_csv(self, filename)
Loads a CSV file and returns its contents as a list of dictionaries.

    Parameter filename: The CSV file name to read.

    Returns: List of dictionaries representing each row in the CSV.
    
Table Class

Handles data manipulation for a list of dictionaries (table-like data).

__init__(self, text, table)
Initializes the Table with a text label and a list of dictionaries.

Attribute text: Placeholder text (currently unused).

Attribute table: Stores the processed list of dictionaries; numeric values are automatically converted to float.

__float_table(self, list_item)
Converts all values in the dictionary list that can be cast to float. Non-numeric values remain unchanged.

Parameter list_item: List of dictionaries to process.

Returns: New list of dictionaries with numeric values converted to float.

filter(self, condition=lambda x: x)
Filters the table according to a custom condition and returns a new Table object containing only matching rows.

Parameter condition: A function applied to each row to determine if it should be included. Default returns all rows.

aggregate(self, aggregate_function, aggregate_key)
Runs a function on all values of a selected key in the table.

Parameter aggregate_function: Function to apply (e.g., sum, max, len).

Parameter aggregate_key: The key in each dictionary on which to run the function.

Returns: Result of the aggregation function.


Project/
│
├── README.md                 # This file
├── Cities.csv                # The dataset
└── data_processing.py        # The analysis code

How to Run and Test

1.Run the data_processing.py script.
2.Modify the lambda functions in the filter and aggregate methods to explore different queries.
3.Ensure your conditions and keys match the structure of your CSV file.