def show_books(library):
    print("\n--- All Books ---")
    if not library:
        print("No books in library.")
        return

    print(f"{'No.':<5} {'Book Name':<30} {'Status'}")
    print("-" * 60)
    for i, book in enumerate(library, 1):
        status = "Available" if book['available'] else f"Unavailable (Issued to: {book['issued_to']})"
        print(f"{i:<5} {book['name']:<30} {status}")
