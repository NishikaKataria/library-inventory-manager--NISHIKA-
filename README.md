# library-inventory-manager--NISHIKA-
A simple Python-based Library Inventory Manager that allows adding, viewing, issuing, returning, and searching books using ISBN or title. The program also saves and loads data from a text file.
---

## 🎯 Features Implemented (As Required in Assignment)
- Add a new book (title, author, ISBN)
- Display all books in the library
- Search books by **title**
- Search books by **ISBN**
- Issue a book (changes status to “Issued”)
- Return a book (changes status back to “Available”)
- Prevent duplicate ISBN entries
- Save book data to `library.txt`
- Load book data automatically when program starts
- Simple, clear, beginner-friendly CLI (menu system)
---

## 🗂 File Used for Storage
The program uses a text file named **`library.txt`** to store all books.

Each line in the file is saved as:
title,author,isbn,status
Example:Math Basics,R.S. Sharma,111,Available

The program automatically:
- Loads this file at the start  
- Updates it whenever you add/issue/return a book  

---

## ▶️ How to Run the Program
1. Create a folder named **library_manager**
2. Inside it, create a file named **library_manager.py**
3. Paste the full code I used in this file
4. Run using:python library_manager.py
## 📌 Menu Options
When you run the program, you will see:
Add Book
View Books
Issue Book
Return Book
Search by Title
Search by ISBN
Exit
You can choose any option by entering the number.

---

## 📚 Sample RuN
Library Menu
Add Book
View Books
Issue Book
Return Book
Search by Title
Search by ISBN
Exit
Enter your choice (1-7): 1

Title: Python Basics
Author: A. Sharma
ISBN: 123
Book added successfully.
Issuing the book:
Enter ISBN to issue: 123
Book issued successfully.
---

## 🧑‍💻 Project Structure
library_manager/
│
└── library_manager.py # main program
└── library.txt # auto-created when books are added
---

## ✔️ Academic Integrity
This project is written in **simple, original, understandable code**, suitable for a first-year student.

---

**Thank you for checking my project!**

