import pytest
import visitor
import book

my_visitor = visitor.Visitor(123456, "Vasiliy", "Ivanovich",
                             "parazit@gmail.com")
my_book = book.Book('Turgenev', 1978, '978-5-389-01985-0')
my_book2 = book.Book('Turgenev2', 1222, '978-5-389-01985-2')


def test_return_visitor():
    """Check return data. If I call create Visitor(1234, "vasil' .....)

    Then instance return expected by me data.
    """

    # Create test visitor

    first_name = my_visitor.first_name
    last_name = my_visitor.last_name
    email = my_visitor.email
    visitor_id = my_visitor.visitor_id
    """Add book in backpack"""
    my_visitor.add_in_backpack(my_book)
    my_visitor.add_in_backpack(my_book2)
    used_book = my_visitor.used_books

    # Check return data
    assert first_name == "Vasiliy"
    assert last_name == "Ivanovich"
    assert email == "parazit@gmail.com"
    assert visitor_id == 123456
    assert used_book == [my_book, my_book2]
