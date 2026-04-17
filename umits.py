import unittest

# Helper functions (input() bypass karne ke liye)
def add_book_direct(library, name):
    for book in library:
        if book['name'].lower() == name.lower():
            return
    library.append({'name': name, 'available': True, 'issued_to': None})

def issue_book_direct(library, name, user):
    for book in library:
        if book['name'].lower() == name.lower() and book['available']:
            book['available'] = False
            book['issued_to'] = user
            return

def return_book_direct(library, name):
    for book in library:
        if book['name'].lower() == name.lower() and not book['available']:
            book['available'] = True
            book['issued_to'] = None
            return


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = []

    def test_add_book(self):
        add_book_direct(self.library, "Python Basics")
        self.assertEqual(len(self.library), 1)
        self.assertEqual(self.library[0]['name'], "Python Basics")

    def test_issue_book(self):
        add_book_direct(self.library, "Python Basics")
        issue_book_direct(self.library, "Python Basics", "Rahul")
        self.assertFalse(self.library[0]['available'])
        self.assertEqual(self.library[0]['issued_to'], "Rahul")

    def test_return_book(self):
        add_book_direct(self.library, "Python Basics")
        issue_book_direct(self.library, "Python Basics", "Rahul")
        return_book_direct(self.library, "Python Basics")
        self.assertTrue(self.library[0]['available'])
        self.assertIsNone(self.library[0]['issued_to'])

    def test_duplicate_book(self):
        add_book_direct(self.library, "Python Basics")
        add_book_direct(self.library, "Python Basics")
        self.assertEqual(len(self.library), 1)


if __name__ == "__main__":
    unittest.main()
