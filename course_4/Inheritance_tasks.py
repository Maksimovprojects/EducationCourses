class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)


class PaperBook(Book):
    def __init__(self, title, author, numPages):
        Book.__init__(self, title, author)
        self.numPages = numPages


class EBook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def getNumBook(self):
        return len(self.books)


myBook = EBook("The Odyssey", "Homer", 2)
myPaperBook = PaperBook("The Odyssey", "Homer", 500)
aadl = Library()
aadl.addBook(myBook)
aadl.addBook(myPaperBook)
print(aadl.getNumBook())

print(myBook.size)
print(myPaperBook.numPages)
