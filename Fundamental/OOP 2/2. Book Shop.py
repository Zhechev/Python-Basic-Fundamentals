class Book:
    title = None
    author = None
    price = None

    def __init__(self, title, author, price):
        self.set_title(title)
        self.set_author(author)
        self.set_price(price)


    def set_title(self, title):
        if len(title) < 3:
            raise Exception("Title not valid!")
        self.title = title

    def set_author(self, author):
        author_parts = author.split(' ')
        if len(author_parts) > 1:
            if author_parts[1][0].isdigit():
                raise Exception("Author not valid!")
        self.author = author

    def set_price(self, price):
        if price <= 0:
            raise Exception("Price not valid!")
        self.price = price

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def __str__(self):
        return f"Type: {type(self).__name__}\nTitle: {self.get_title()}\nAuthor: {self.get_author()}\nPrice: {self.get_price():.2f}"


class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author, price)
        self.set_price(price)

    def set_price(self, price):
        self.price = price * 1.3


author = input()
title = input()
price = float(input())

try:
    book = Book(title, author, price)
    golden_book = GoldenEditionBook(title, author, price)
    print(book)
    print()
    print(golden_book)
except Exception as e:
    print(e)
