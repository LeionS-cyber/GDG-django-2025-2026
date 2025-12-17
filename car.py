class Car:
    def __init__(self, make):
        self.make = make

    def get_make(self):
        return self.make

# Testing with an object
my_car = Car("Toyota")
print(f"Car Make: {my_car.get_make()}")
