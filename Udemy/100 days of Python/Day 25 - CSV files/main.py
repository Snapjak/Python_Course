# import csv
import pandas

# with open("/home/jeremy/repos/Udemy/100 days of Python/Day 25 - CSV files/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
# #         if row[1] != "temp":
# #             temp = int(row[1])
# #             temperatures.append(temp)
# #     print(temperatures)
     
# from numpy.lib.function_base import average

# data = pandas.read_csv("/home/jeremy/repos/Udemy/100 days of Python/Day 25 - CSV files/weather_data.csv")
# temperature = data["temp"]
# print(temperature.mean())


# print(temperature.max())

# print(data[data.temp == temperature.max()])


# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)

# monday_f = monday_temp * 9/5 + 32
# print(monday_f)

data = pandas.read_csv("/home/jeremy/repos/Udemy/100 days of Python/Day 25 - CSV files/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirels_color = data["Primary Fur Color"]

gray_squirels = data[squirels_color == "Gray"]
count_gray = len(gray_squirels)

cinnamon_squirels = data[squirels_color == "Cinnamon"]
count_cinnamon = len(cinnamon_squirels)

black_squirels = data[squirels_color == "Black"]
count_black = len(black_squirels)

data_dict = {
    "Color": ["Grey", "Cinnamon", "Black"],
    "Count": [count_gray, count_cinnamon, count_black],
}

subset = pandas.DataFrame(data_dict)
subset.to_csv("squirels_colors.csv")
print(subset)










