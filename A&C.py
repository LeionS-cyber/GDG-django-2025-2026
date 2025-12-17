class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Testing both
generic_animal = Animal()
my_cat = Cat()

generic_animal.make_sound()
my_cat.make_sound()
