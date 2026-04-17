def add_book(library):
    print("\n--- Add Book ---")
    name = input("Book Name: ")

    for book in library:
        if book['name'].lower() == name.lower():
            print("Book already exists!")
            return

    library.append({
        'name': name,
        'available': True,
        'issued_to': None
    })
    print(f"Book '{name}' added successfully!")
