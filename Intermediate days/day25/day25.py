
# with open("C:\\Users\\vinic\\OneDrive\\CODE\\PY\\A100DAYSOFCODE\\Intermediate days\\day25\\weather_data.csv", "r") as file:
#     data = file.readlines()
#     list = []
#     for i in data:    
#         list.append(i.strip())
#     print(list)
    
# import csv

# with open("Intermediate days\\day25\\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp": temperatures.append(row[1])
#     print(temperatures)

import pandas as pd

data = pd.read_csv("Intermediate days\\day25\\weather_data.csv")
print(data)