# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)

# import csv
#
# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#
#     temp = []
#     for data in data:
#         a = data[1]
#         if data[1] != "temp":
#             temp.append(int(data[1]))
#
#     print(temp)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)