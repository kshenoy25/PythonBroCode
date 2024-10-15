# super()= function used in a child class to call methods from a parent class (superclass)
#           allows you to extend the functionality of the inherited methods


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)

        #self.color = color
        #elf.filled = is_filled
        self.radius = radius

    # method overriding in action
    def describe(self):
        # extending the functionality of the describe method
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")



class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)

        #self.color = color
        #self.filled = is_filled
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)

        #self.color = color
        #self.filled = is_filled
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()


circle = Circle(color = "red", is_filled = True, radius = 5)
square = Square(color = "blue", is_filled = False, width = 6)
triangle = Triangle(color = "green", is_filled = True, width = 4, height = 8)

#print(circle.color)
#print(circle.is_filled)
#print(circle.radius)
#print(f"{circle.radius}cm")

#print("************************************************")

#print(square.color)
#print(square.is_filled)
#print(square.width)
#print(f"{square.width}cm")


#print(triangle.color)
#print(triangle.is_filled)
#print(triangle.width)
#print(f"{triangle.width}cm")
#print(f"{triangle.height}cm")

square.describe()
