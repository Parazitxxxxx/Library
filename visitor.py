import re


class Visitor:

    # Class show human which come in library.

    def __init__(self):
        # usedBooks_id - saved which books used visitors
        self._used_books_id = []

    def create_visitor(self, visitor_id, name, email):

        if not isinstance(name, int) and name != "" and \
                3 < len(str(name)) < 15 and not name.isdigit():
            self._name = name
        else:
            raise Exception("Delivered empty name or not expected \
                                quantity symbols in name or they is digit")

        if not isinstance(visitor_id, str) and visitor_id != "" and \
                3 < len(str(abs(visitor_id))) < 15:
            self._visitor_id = visitor_id
        else:
            raise Exception("Delivered empty name or not expected \
                                quantity symbols in name or they is digit")

        # EMAIL
        # Mask for email
        reg = '(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)'
        email = email.lower()
        if email != "" and 3 < len(str(email)) < 64 and \
                re.fullmatch(reg, email):
            self._email = email
        else:
            raise Exception("!Delivered empty  Email or bad Email address")

        # Check and saved this which books used visitors

    def add_book_id(self, *used_books_id):

        for book_id in used_books_id:
            if not isinstance(book_id, str) and book_id != "" and \
                    3 < len(str(abs(book_id))) < 10:
                self._used_books_id.append(book_id)
            else:
                raise Exception("Delivered empty usedBookID or not\
                                    expected quantity symbols in usedBookID")

    def get_name(self):
        return self._name

    def get_id(self):
        return self._visitor_id

    def get_email(self):
        return self._email

    def get_used_books_id(self):
        return self._used_books_id

    def delete_used_book_id(self, del_book_id ):
        self._used_books_id.remove(del_book_id)

    def get_status(self):
        return 'id:', self._visitor_id, 'name: ', self._name, 'email :', \
               self._email, 'used_books_id:', self._used_books_id




