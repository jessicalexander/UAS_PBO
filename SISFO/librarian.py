from datetime import datetime
import os
from logger import log_activity
from base.User import User

class Librarian(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(current_dir, 'db', 'borrow_return_book.txt') 
    
    @log_activity
    def add_books(self, books, library):
        if isinstance(books, list):
            library.books.extend(books)
        else:
            library.books.append(books)

    # Assuming students will go to UKRIDA to physically take the book
    @log_activity
    def borrow_book(self, name, book):
        timestamp = datetime.now()
        formatted_timestamp = timestamp.strftime("%Y-%m-%d")
        borrowing_info = f'User {name} has borrowed the book "{book}" on {formatted_timestamp}\n'
        with open(self.file_path, 'a') as f:
            f.write(borrowing_info)
    
    @log_activity
    def return_book(self, name, book):
        timestamp = datetime.now()
        formatted_timestamp = timestamp.strftime("%Y-%m-%d")
        returned_info = f'User {name} has returned the book "{book}" on {formatted_timestamp}\n'
        with open(self.file_path, 'a') as f:
            f.write(returned_info)
