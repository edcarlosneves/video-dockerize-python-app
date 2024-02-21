import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_circumference_length(self):
        return 2 * math.pi * self.radius

    def calculate_area_of_sector(self, central_angle):
        if central_angle <= 360:
            return (central_angle / 360) * self.calculate_area()
        raise ValueError("The central angle must be less than or equal to 360")
