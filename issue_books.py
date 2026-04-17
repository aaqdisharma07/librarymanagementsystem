def issue_book(library):
    print("\n--- Issue Book ---")
    if not library:
        print("No books in library.")
        return

    name = input("Enter Book Name to Issue: ")
    user = input("Enter Your Name: ")

    for book in library:
        if book['name'].lower() == name.lower():
            if book['available']:
                book['available'] = False
                book['issued_to'] = user
                print(f"Book '{name}' issued to {user} successfully!")
            else:
                print(f"Sorry! Book '{name}' is already issued to {book['issued_to']}.")
            return

    print(f"Book '{name}' not found in library.")
