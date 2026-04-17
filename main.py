from add_books import add_book
from show_books import show_books
from issue_books import issue_book
from return_books import return_book

library = []

def main():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            show_books(library)
        elif choice == '3':
            issue_book(library)
        elif choice == '4':
            return_book(library)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
