# magic methods = dunder methods (double underscore) __init__, __str__, __eq__
#                 they are automatically called by many of Python's built-in operations
#                 they allow developers to define or customize the behavior of objects



class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"




book1 = Book("The Howler", "T.S. Williams", 156)
book2 = Book("Love", "Jackie Doyle", 334)
book3 = Book("The Fellowship of the Ring", "J.R.R Tolkien", 224)

print("Doyle" in book2)
print(book1["title"])
print(book2["author"])
print(book2["num_pages"])

print(book1["audio"])