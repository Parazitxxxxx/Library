import book as Book


class Visitor:
    """Class made for visitor in library.

    Class show human which come in library.
    For create visitor use: Visitor(id, first_name, last_name, email)
    Add and del books in visitor backpack: add_in_backpack(), del_of_backpack
    Get data about visitor, use fields: visitor_id, first_name, last_name,
    email.
    For get data about all books in backpack use fields: used_books, which
    return list: (instance Book)
    """
    def __init__(self, visitor_id: int, first_name: str,
                 last_name: str, email: str):

        self.visitor_id = visitor_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        """ this list saved which books used visitors"""
        self.used_books = []

    def add_in_backpack(self, used_book:Book):
            """Adding instance new used book for backpack visitor"""
            self.used_books.append(used_book)

    def del_of_backpack(self, del_book):
        """Deleting instance used book for visitor"""
        self.used_books.remove(del_book)
