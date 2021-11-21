class Car:
    def __init__(self):
        self.car_brand = None
        self.car_power = None
        self.car_color = None
        self.x_position = 5
        self.y_position = 5
    def drive(self, x, y):
        self.x_position += x
        self.y_position += y



car1 = Car()

print(car1.y_position)
print(car1.x_position)

