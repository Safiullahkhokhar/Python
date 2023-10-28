# Library Management Software

# Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and show how you
# can print all books, add a book and get the number of books using different methods.
# Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    def addBooks(self, book):
        self.books.append(book)
        self.noBooks= len(self.books)
    def show(self):
        print(f"The Library has {self.noBooks} books.The books are ")
        for book in self.books:
            print(book)

obj1= Library()
obj1.addBooks("WhoAmI")
obj1.addBooks("WalkWithMe")
obj1.addBooks("HelpOut")
obj1.show()