class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object and printing attributes
person1 = Person("Alice", 25)
print(f"Name: {person1.name}, Age: {person1.age}")
