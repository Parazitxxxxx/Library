import re


class Visitor:
    """Class made for library.

    Class show human which come in library.
    For create visitor use: create_visitor()
    Add and delete books in class visitor: add_book_id(), delete_used_book_id
    Get data about visitor, use: get_name/ id/ email/ used_book_id()
    """

    # Mask for email
    reg = '(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)'

    def __init__(self):
        """ this list saved which books used visitors"""
        self._used_books_id = []

        # restriction length data
        self._min_length_data = 3
        self._max_length_data = 15
        self._max_length_email = 64

    def create_visitor(self, visitor_id, name, email):
        """Create visitor in library and test his data."""

        if isinstance(name, str) and name != "" and self._min_length_data <\
                len(str(name)) < self._max_length_data:
            self._name = name
        else:
            raise ValueError("Delivered empty name or not expected \
                                quantity symbols in name or they is digit")

        if isinstance(visitor_id, int) and visitor_id != "" and \
                self._min_length_data < len(str(abs(visitor_id))) < \
                self._max_length_data:
            self._visitor_id = visitor_id
        else:
            raise ValueError("Delivered empty name or not expected \
                                quantity symbols in name or they is digit")

        # EMAIL

        email = email.lower()
        if email != "" and self._min_length_data < len(str(email)) <\
                self._max_length_email and re.fullmatch(self.reg, email):
            self._email = email
        else:
            raise Exception("!Delivered empty  Email or bad Email address")

        # Check and saved this which books used visitors

    def add_book_id(self, *used_books_id):
        """Adding ID new used book for visitor"""

        for book_id in used_books_id:
            if isinstance(book_id, int) and book_id != "" and \
                    self._min_length_data < len(str(book_id)) <\
                    self._max_length_data:
                self._used_books_id.append(book_id)
            else:
                raise ValueError("Delivered empty usedBookID or not\
                                    expected quantity symbols in usedBookID")

    def delete_used_book_id(self, del_book_id):
        """Deleting ID used book for visitor"""
        self._used_books_id.remove(del_book_id)

    """Next four metods return data about visitor"""
    def get_name(self):
        return self._name

    def get_id(self):
        return self._visitor_id

    def get_email(self):
        return self._email

    def get_used_books_id(self):
        return self._used_books_id





