def return_book(library):
    print("\n--- Return Book ---")
    if not library:
        print("No books in library.")
        return

    name = input("Enter Book Name to Return: ")

    for book in library:
        if book['name'].lower() == name.lower():
            if not book['available']:
                print(f"Book '{name}' returned successfully (was issued to {book['issued_to']}).")
                book['available'] = True
                book['issued_to'] = None
            else:
                print(f"Book '{name}' was not issued to anyone.")
            return

    print(f"Book '{name}' not found in library.")
