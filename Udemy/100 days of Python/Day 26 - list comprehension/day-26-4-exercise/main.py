sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
list_strings = sentence.split()

result= {item:len(item) for item in list_strings}

print(result)

## exercise 2

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {weekday:temp_c*9/5+32 for (weekday, temp_c) in weather_c.items()}

print(weather_f)