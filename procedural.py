# Procedural Library Management System

# Data stored in global lists
book_titles = []
book_authors = []
book_isbns = []
book_statuses = []  # True for available, False for checked out
book_checkout_dates = []

def add_book():
    """Adds a new book to the library catalog."""
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    isbn = input("Enter the ISBN: ")
    
    book_titles.append(title)
    book_authors.append(author)
    book_isbns.append(isbn)
    book_statuses.append(True)  # Initially available
    book_checkout_dates.append(None) # No checkout date yet
    print(f"\nBook '{title}' added successfully!")
    print("-" * 30)

def display_all_books():
    """Displays all books in the catalog."""
    print("\n--- All Books in the Catalog ---")
    if not book_titles:
        print("The catalog is empty.")
    else:
        for i in range(len(book_titles)):
            status = "Available" if book_statuses[i] else "Checked Out"
            checkout_date_info = f" (Checked out on: {book_checkout_dates[i]})" if not book_statuses[i] and book_checkout_dates[i] else ""
            print(f"Title: {book_titles[i]}")
            print(f"Author: {book_authors[i]}")
            print(f"ISBN: {book_isbns[i]}")
            print(f"Status: {status}{checkout_date_info}")
            print("-" * 30)

def search_for_book():
    """Searches for a book by title or author."""
    query = input("Enter a title or author to search: ").lower()
    print("\n--- Search Results ---")
    found = False
    for i in range(len(book_titles)):
        if query in book_titles[i].lower() or query in book_authors[i].lower():
            status = "Available" if book_statuses[i] else "Checked Out"
            checkout_date_info = f" (Checked out on: {book_checkout_dates[i]})" if not book_statuses[i] and book_checkout_dates[i] else ""
            print(f"Title: {book_titles[i]}")
            print(f"Author: {book_authors[i]}")
            print(f"ISBN: {book_isbns[i]}")
            print(f"Status: {status}{checkout_date_info}")
            print("-" * 30)
            found = True
    if not found:
        print("No books found matching your query.")
    print("-" * 30)

def checkout_book():
    """Checks out a book by its ISBN."""
    isbn_to_checkout = input("Enter the ISBN of the book to check out: ")
    date_to_checkout = input("Enter today's date (YYYY-MM-DD): ")
    found = False
    for i in range(len(book_isbns)):
        if book_isbns[i] == isbn_to_checkout:
            if book_statuses[i]:
                book_statuses[i] = False  # Set to checked out
                book_checkout_dates[i] = date_to_checkout
                print(f"\nBook '{book_titles[i]}' checked out successfully!")
            else:
                print(f"\nBook '{book_titles[i]}' is already checked out.")
            found = True
            break
    if not found:
        print("Book with that ISBN not found.")
    print("-" * 30)
    
def return_book():
    """Returns a book by its ISBN."""
    isbn_to_return = input("Enter the ISBN of the book to return: ")
    found = False
    for i in range(len(book_isbns)):
        if book_isbns[i] == isbn_to_return:
            if not book_statuses[i]:
                book_statuses[i] = True  # Set to available
                book_checkout_dates[i] = None # Reset checkout date
                print(f"\nBook '{book_titles[i]}' returned successfully!")
            else:
                print(f"\nBook '{book_titles[i]}' is already available.")
            found = True
            break
    if not found:
        print("Book with that ISBN not found.")
    print("-" * 30)


"""Displays the main menu and handles user input."""
while True:
    print("\n--- Library System Menu ---")
    print("1. Add a new book")
    print("2. Display all books")
    print("3. Search for a book")
    print("4. Check out a book")
    print("5. Return a book")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_book()
    elif choice == '2':
        display_all_books()
    elif choice == '3':
        search_for_book()
    elif choice == '4':
        checkout_book()
    elif choice == '5':
        return_book()
    elif choice == '6':
        print("Exiting the library system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")