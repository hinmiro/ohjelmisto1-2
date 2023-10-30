class Publish:

    def __init__(self, name):
        self.name = name


class Book(Publish):

    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_info(self):
        print(f"Name: {self.name}\nAuthor: {self.author}\nPages: {self.pages}\n===========")


class Magazine(Publish):

    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        print(f"Name: {self.name}\nEditor: {self.editor}\n===========")


publ1 = Magazine("Aku Ankka", "Aki Hyyppä")
publ2 = Book("Hytti n:o 6", "Rosa Liksom", 200)

publ1.print_info()
publ2.print_info()
