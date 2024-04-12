class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = True  # initially the book is available

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book.title} has been removed from the library.")

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def search_book_by_author(self, author):
        author_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                author_books.append(book)
        return author_books

    def display_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available Books: ")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books available!")


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print("This book is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} has returned '{book.title}'")
        else:
            print("You have not borrowed this book.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book}")
        else:
            print("You have not borrowed any books.")


class Transaction:
    @staticmethod
    def display_transaction_history(member):
        print(f"The transaction history for {member.name}")
        if member.borrowed_books:
            print("Borrowed Books:")
            for book in member.borrowed_books:
                print(f"- Borrowed '{book.title}'")
        else:
            print("No transaction history.")


if __name__ == "__main__":
    # Create some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Fiction")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Fiction")
    book3 = Book("1984", "George Orwell", "9780451524935", "Dystopian")

    # Create a library and add books to it
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Display available books in the library
    library.display_available_books()

    # Create a member and let them borrow a book
    member = Member("Alice", "1001")
    member.borrow_book(book1)

    # Display member's borrowed books and library's available books
    member.display_borrowed_books()
    library.display_available_books()

    # Let the member return the book
    member.return_book(book1)

    # Display member's borrowed books and library's available books after return
    member.display_borrowed_books()
    library.display_available_books()

    # Display transaction history for the member
    Transaction.display_transaction_history(member)
