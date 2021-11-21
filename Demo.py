class Car:
    def __init__(self):
        self.car_brand = None
        self.car_power = None
        self.car_color = None

car1 = Car()

print(car1.car_brand)
car1.car_brand = "Toyota"
print(car1.car_brand)
car1.car_color = "Blau"
print(car1.car_color)
