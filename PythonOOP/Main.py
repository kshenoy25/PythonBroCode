from car import Car

car_1 = Car("Chevy", "Corvette", 2024, "Blue")
car_2 = Car("Ford", "Mustang", 2023, "Black")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print("-----------")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

print("-----------")

car_1.drive()
car_1.stop()

print("-----------")

car_2.drive()
car_2.stop()