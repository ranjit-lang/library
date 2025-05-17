import sqlite3


conn = sqlite3.connect("library.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        available INTEGER DEFAULT 1
    )
''')
conn.commit()

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    print("Book added successfully!")

def display_books():
    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Available: {'Yes' if row[3] else 'No'}")

def borrow_book():
    book_id = int(input("Enter book ID to borrow: "))
    cursor.execute("SELECT available FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()
    if book and book[0] == 1:
        cursor.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        conn.commit()
        print("Book borrowed successfully!")
    else:
        print("Book not available or does not exist.")

def return_book():
    book_id = int(input("Enter book ID to return: "))
    cursor.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
    conn.commit()
    print("Book returned successfully!")

def remove_book():
    book_id = int(input("Enter book ID to remove: "))
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    print("Book removed from library.")

def menu():
    while True:
        print("\n--- Library Management ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Remove Book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            remove_book()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()


conn.close()
