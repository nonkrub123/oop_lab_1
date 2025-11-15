import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data
    

class DB:
    """Handle mutiple table data"""

    def __init__(self):
        """Initialize the Database with a blank list"""
        self.table = []
    
    def insert(self, table_list):
        """Insert an table object in table property"""
        self.table.append(table_list)
    
    def search(self,table_name):
        """Return Table obj using table name. otherwise return new Table object with blank list"""
        for list_table in self.table:
            if list_table.name == table_name:
                return Table(table_name,list_table.table)
            
        return Table(table_name,[])
    

class Table:

    def __init__(self,name,table):
        """Initialize the Table class with a dict list and name"""
        self.name = name
        self.table = table
        
    def __float_table(self, list_item):
        """Return list including every value in dict list that's able to be float to float. 
        Otherwise it stay the same"""
        new_table = []
        for item in list_item:
            new_row = {}
            for key in item.keys():
                try:
                    new_row[key] = float(item[key])
                except ValueError:
                    new_row[key] = item[key]
            new_table.append(new_row)
        return new_table
    
    def turn_table_float(self):
        """set table attributes by calling __float_table method"""
        self.table = self.__float_table(self.table)

    def filter(self,condition = lambda x:x):
        """Filter our dict list with custom condition and 
        return new object of Table with new list filtered"""
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
                
        return Table(f"{self.name}_filtered", filtered_list)
    
    def aggregate(self, aggregate_function, aggregate_key,):
        """Run a function on a list of the dict list from input key"""
        self.turn_table_float()
        select_list = [item[aggregate_key] for item in self.table if aggregate_key in item.keys()]
        result = aggregate_function(select_list)
        return result
    
    def join(self,input_table, joined_key):
        """Join another table obj with current table obj then return new joined table obj"""
        joined_list = []
        for item in self.table:
            if joined_key in item.keys():
                joined_list.append(item)
                index = len(joined_list) - 1
                for compare in input_table.table:
                    if compare[joined_key] == item[joined_key]:
                        for add_key in compare.keys():
                            if add_key != joined_key:
                                joined_list[index][add_key] = compare[add_key]
                            else:
                                pass
                        continue
            else:
                joined_list.append(item)

        return Table(f"{self.name}_joined", joined_list)


    def __str__(self):
        return self.name + ':' + str(self.table)

loader = DataLoader()
cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)
countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search('cities')
print("List all cities in Italy:") 
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
print()

my_table2 = my_DB.search('countries')
print("List all non-EU countries:") 
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print(my_table3_filtered.table)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()