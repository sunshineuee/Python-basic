class Road:
    def __init__(self, length, width, depth):
        self.__length = length
        self.__width = width
        self.__depth = depth

    def asphalt_mass(self):
        mass = self.__width * self.__length * self.__depth * 25 / 1000
        mass = int(mass)
        print(mass)


road = Road(20, 5000, 5)
road.asphalt_mass()