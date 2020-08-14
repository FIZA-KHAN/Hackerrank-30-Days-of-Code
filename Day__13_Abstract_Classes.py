

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Price: {price}")


