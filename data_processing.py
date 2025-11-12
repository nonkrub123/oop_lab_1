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
    
class Table:
    """"""

    def __init__(self,text,table):
        """Initialize the Table class with a dict list and text"""
        self.text = text
        self.table = self.__float_table(table)

    def __float_table(self, list_item):
        """Turn every value in dict list that's able to be float to float. 
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
    
    def filter(self,condition = lambda x:x):
        """Filter our dict list with custom condition and 
        return new object of Table with new list filtered"""
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
                
        return Table('cities', filtered_list)
    
    def aggregate(self, aggregate_function, aggregate_key,):
        """Run a function on a list of the dict list from input key"""
        select_list = [item[aggregate_key] for item in self.table if aggregate_key in item.keys()]
        result = aggregate_function(select_list)
        return result

loader = DataLoader()
cities = loader.load_csv('Cities.csv')
my_table1 = Table('cities', cities)

# Print the average temperature of all the cities
my_value = my_table1.aggregate(lambda x: sum(x)/len(x), 'temperature')
print(f"{my_value}")
print()

# Print all cities in Germany
my_cities = my_table1.filter(lambda x: x['country'] == 'Germany')
cities_list = [[city['city'], city['country']] for city in my_cities.table]
print("All the cities in Germany:")
for city in cities_list:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
my_cities = my_table1.filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12.0)
cities_list = [[city['city'], city['country'], city['temperature']] for city in my_cities.table]
print("All the cities in Spain with temperature above 12°C:")
for city in cities_list:
    print(city)
print()

# Count the number of unique countries
my_countries = my_table1.aggregate(lambda x: len(set(x)), 'country')
print("The number of unique countries is:")
print(my_countries)
print()

# Print the average temperature for all the cities in Germany
my_value = my_table1.filter(lambda x: x['country'] == 'Germany').aggregate(lambda x: sum(x)/len(x), 'temperature')
print("The average temperature of all the cities in Germany:")
print(my_value)
print()

# Print the max temperature for all the cities in Italy
my_value = my_table1.filter(lambda x: x['country'] == 'Italy').aggregate(lambda x: max(x), 'temperature')
print("The max temperature of all the cities in Italy:")
print(my_value)
print()
