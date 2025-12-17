class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

    def show_books(self):
        for book in self.books:
            print(f"- {book}")

# Testing
my_library = Library()
my_library.add_book("Python Basics")
my_library.add_book("OOP Masters")
my_library.show_books()
