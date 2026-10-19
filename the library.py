books = [
    {"name": "Python Basics", "available": True},
    {"name": "Clean Code", "available": True},
    {"name": "Computer Networks", "available": True}
]


def show_books():
    print("\n===== Books =====")

    for book in books:
        if book["available"]:
            status = "Available"
        else:
            status = "Borrowed"

        print(book["name"], "-", status)


def add_book():
    name = input("Enter book name: ")

    book = {
        "name": name,
        "available": True
    }

    books.append(book)

    print("Book added successfully!")


def borrow_book():
    name = input("Enter book name to borrow: ")

    for book in books:
        if book["name"].lower() == name.lower():

            if book["available"]:
                book["available"] = False
                print("Book borrowed successfully!")
            else:
                print("This book is already borrowed.")

            return

    print("Book not found.")


def return_book():
    name = input("Enter book name to return: ")

    for book in books:
        if book["name"].lower() == name.lower():

            if not book["available"]:
                book["available"] = True
                print("Book returned successfully!")
            else:
                print("This book is already available.")

            return

    print("Book not found.")


def search_book():
    name = input("Enter book name to search: ")

    for book in books:
        if name.lower() in book["name"].lower():

            if book["available"]:
                status = "Available"
            else:
                status = "Borrowed"

            print(book["name"], "-", status)
            return

    print("Book not found.")


while True:

    print("\n===== Library Management System =====")
    print("1. Show Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_books()

    elif choice == "2":
        add_book()

    elif choice == "3":
        borrow_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        search_book()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")