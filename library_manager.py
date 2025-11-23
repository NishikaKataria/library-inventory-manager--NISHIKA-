# Simple Library Manager (single file)
# Name: Nishika Chaudhary
# Class: B.Tech Ds (1st Year)
# Lab Assignment – Library Inventory Manager

# File where books are stored (each line: title,author,isbn,status)
DATA_FILE = "library.txt"

class Book:
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display(self):
        print(f"{self.title} | {self.author} | {self.isbn} | {self.status}")

def load_books():
    books = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                # handle if file has extra commas by joining extras into title
                if len(parts) >= 4:
                    title = parts[0]
                    author = parts[1]
                    isbn = parts[2]
                    status = parts[3]
                    books.append(Book(title, author, isbn, status))
    except FileNotFoundError:
        # no file yet, start empty
        pass
    return books
def save_all(books):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            for b in books:
                f.write(f"{b.title},{b.author},{b.isbn},{b.status}\n")
    except Exception as e:
        print("Error saving data:", e)

def find_by_isbn(books, isbn):
    for b in books:
        if b.isbn == isbn:
            return b
    return None

def add_book(books):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()
    if find_by_isbn(books, isbn):
        print("ISBN already exists. Book not added.")
        return
    new = Book(title, author, isbn, "Available")
    books.append(new)
    save_all(books)
    print("Book added and saved.")

def list_books(books):
    if not books:
        print("No books found.")
        return
    print("\nTitle | Author | ISBN | Status")
    print("-" * 50)
    for b in books:
        b.display()

def issue_book(books):
    isbn = input("ISBN to issue: ").strip()
    b = find_by_isbn(books, isbn)
    if not b:
        print("Book not found.")
    elif b.status.lower() == "issued":
        print("Book already issued.")
    else:
        b.status = "Issued"
        save_all(books)
        print("Book issued successfully.")

def return_book(books):
    isbn = input("ISBN to return: ").strip()
    b = find_by_isbn(books, isbn)
    if not b:
        print("Book not found.")
    elif b.status.lower() == "available":
        print("Book is already available.")
    else:
        b.status = "Available"
        save_all(books)
        print("Book returned successfully.")

def search_title(books):
    key = input("Enter title keyword: ").strip().lower()
    found = [b for b in books if key in b.title.lower()]
    if not found:
        print("No books match that title.")
    else:
        for b in found:
            b.display()

def search_isbn(books):
    isbn = input("Enter ISBN to search: ").strip()
    b = find_by_isbn(books, isbn)
    if b:
        b.display()
    else:
        print("Book not found.") 

def main():
    books = load_books()
    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search by Title")
        print("6. Search by ISBN")
        print("7. Exit")
        choice = input("Enter choice (1-7): ").strip()
        if choice == "1":
            add_book(books)
        elif choice == "2":
            list_books(books)
        elif choice == "3":
            issue_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            search_title(books)
        elif choice == "6":
            search_isbn(books)
        elif choice == "7":
            print("Exiting... saving data.")
            save_all(books)
            break
        else:
            print("Invalid choice. Enter number 1-7.")

if __name__ == "__main__":
    main()





    
            





           



