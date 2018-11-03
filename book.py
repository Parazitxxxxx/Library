class Book:
    """Class made for show book in library.

    Class show book which was in library.
    For create book use Book(author, year_publish, isbn_book
    For get data about book use fields: author, year_publish, isbn_book
    """
    def __init__(self, author, year_publish, isbn_book):
        self.author = author
        self.year_publish = year_publish
        self.isbn_book = isbn_book
