import re


class Visitor:
    """Class made for library.

    Class show human which come in library.
    For create visitor use: create_visitor()
    Add and del books in visitor backpack: add_in_backpack(), del_of_backpack
    Get data about visitor, use fields:used_books_id, visitor_id,
    name, email

    """

    # Mask for email
    reg = '(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)'

    # restriction length data
    _min_length_data = 3
    _max_length_data = 15
    _max_length_email = 64

    def __init__(self, visitor_id, name, email):
        """ this list saved which books used visitors"""
        self.used_books_id = []

        self.visitor_id = visitor_id
        self.name = name
        self.email = email

    @classmethod
    def create_visitor(cls, visitor_id, name, email):
        """Create visitor in library and test his data."""

        arguments = []

        if isinstance(visitor_id, int) and visitor_id != "" and \
                cls._min_length_data < len(str(abs(visitor_id))) < \
                cls._max_length_data:
            if cls.check_id(visitor_id):
                arguments.append(visitor_id)
            else:
                raise ValueError("Use unique ID!")

        else:
            raise ValueError("Delivered empty name or not expected "
                             "quantity symbols in name or they is digit")

        if isinstance(name, str) and name != "" and cls._min_length_data <\
                len(str(name)) < cls._max_length_data:
            arguments.append(name)
        else:
            raise ValueError("Delivered empty name or not expected "
                             "quantity symbols in name or they is digit")

        # EMAIL

        email = email.lower()
        if email != "" and cls._min_length_data < len(str(email)) <\
                cls._max_length_email and re.fullmatch(cls.reg, email):
            arguments.append(email)
        else:
            raise Exception("!Delivered empty  Email or bad Email address")

        return cls(*arguments)

        # Check and saved this which books used visitors

    # this function check id
    @classmethod
    def check_id(cls, user_id):
        cls.check_id = user_id
        raise NotImplemented("Error !")
    #   return True

    # if ID unique then return TRUE else return FALSE

    def add_in_backpack(self, *used_books_id):
        """Adding ID new used book for backpack visitor"""

        for book_id in used_books_id:
            if isinstance(book_id, int) and book_id != "" and \
                    self._min_length_data < len(str(book_id)) <\
                    self._max_length_data:
                self.used_books_id.append(book_id)
            else:
                raise ValueError("Delivered empty usedBookID or not "
                                 "expected quantity symbols in usedBookID")

    def del_of_backpack(self, del_book_id):
        """Deleting ID used book for visitor"""
        self.used_books_id.remove(del_book_id)
