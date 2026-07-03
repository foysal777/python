import os

class Book:
    def __init__(self, title, author , quantity):
        self.title = title
        self.author = author
        self.quantity = int(quantity)



    def to_file_format(self):
        return f"{self.title},{self.author},{self.quantity}\n"
    



class Library:
    def __init__(self):
        self.file_name = "library_db.txt"
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as file:
                pass


    def add_book(self, book):
        with open(self.file_name, "a") as file:
            pass


    def view_books(self):
        with open(self.file_name, "a") as file:
            pass
    

    def view_books(self):
        with open(self.file_name, "r") as file:
            books = file.readlines()
            if not books:
                print("Library is empty.")
            else:
                for book in books:
                    title, author, quantity = book.strip().split(",")
                    print(f"Title: {title}, Author: {author}, Quantity: {quantity}")
