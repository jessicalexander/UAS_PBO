class Book:
    def __init__(self, title, author, genre, content=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.content = content

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"
    