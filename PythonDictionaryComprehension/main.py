# dictionary comprehension = create dictionaries using an expression that can replace for loops and certain
#                            lambda functions
# dictionary = {key: expression for (key,value) in iterable}

# --------------------------------------------------------------------------------------
#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 70, 'Chicago': 50,}

#ities_in_C = {key: round((value - 32) * (5/9)) for (key, value) in cities_in_F.items()}
#print(cities_in_C)

#--------------------------------------------------------------------------------------

#weather = {'New York': "Sunny", 'Boston': "Cloudy", 'Los Angeles': "Sunny", 'Chicago':"Rainy" }

#sunny_weather = {key: value for (key,value) in weather.items() if value == "Sunny"}

#print(sunny_weather)

#--------------------------------------------------------------------------------------
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50,}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}

#desc_cities = {key: ("WARM" if value >= 40  else "COLD") for (key,value) in cities.items()}

print(desc_cities)
