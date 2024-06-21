from logger import log_activity

class Library:
    def __init__(self):
        self._name = "E-Library UKRIDA"
        self.books = []
    
    def get_book_results(self, keyword):
        results = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword.lower() in book.genre.lower():
                results.append(book)
        if not results:
            print('Book not found, please search by book title or author or genre')
        else:
            for book in results:
                print(book)

    def get_book_content(self, keyword):
        found = False
        for book in self.books:
            if keyword.lower() == book.title.lower():
                found = True
                if book.content == None:
                    print(f'There is no e-book version of {book.title}, you can borrow the book in UKRIDA')
                else:
                    print(book.content)
        if not found:
            print('Book not found, please search by the book title')
