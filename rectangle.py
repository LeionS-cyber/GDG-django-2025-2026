class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(10, 5)
# Printing area without a separate method
print(f"Area: {rect.width * rect.height}")
