import pytest
import visitor
visitor = visitor.Visitor()


def test_return_visitor():
    """Check return data. If I call create_visitor(1234, "vasil' .....)

    Then class return expected by me data.
    """

    # Create test visitor
    visitor.create_visitor(123456, "Vasiliy", "parazit@gmail.com")
    name = visitor.get_name()
    email = visitor.get_email()
    visitor_id = visitor.get_id()
    visitor.add_book_id(1234, 5678, 9101112, 7889)
    used_book_id = visitor.get_used_books_id()

    # Check return data
    assert name == "Vasiliy"
    assert email == "parazit@gmail.com"
    assert visitor_id == 123456
    assert used_book_id == [1234, 5678, 9101112, 7889]

# If delivered empty.


def test_passes_id():
    with pytest.raises(Exception):
        visitor.create_visitor(" ", "dsds", "parazit@gmail.com")


def test_passes_name():
    with pytest.raises(Exception):
        visitor.create_visitor(123456, " ", "parazit@gmail.com")


def test_passes_email():
    with pytest.raises(Exception):
        visitor.create_visitor(123456, "dsds", " ")


def test_passes_user_book_id():
    with pytest.raises(Exception):
        visitor.add_book_id(" ")


# If delivered short.

def test_passes_id_short():
    with pytest.raises(Exception):
        visitor.create_visitor(123, "Vasiliy", "parazit@gmail.com")


def test_passes_name_short():
    with pytest.raises(Exception):
        visitor.create_visitor(123456, "Vas", "parazit@gmail.com")


def test_passes_email_short():
    with pytest.raises(Exception):
        visitor.create_visitor(123456, "Vasiliy", "par")


def test_passes_user_book_id_short():
    with pytest.raises(Exception):
        visitor.add_book_id(12)

# If delivered long.


def test_passes_id_long():
    with pytest.raises(Exception):
        visitor.create_visitor(123478988567891, "Vasiliy", "parazit@gmail.com")


def test_passes_name_long():
    with pytest.raises(Exception):
        visitor.create_visitor(123456, "Vasiluiiygrtdefrt", "parazit@gmail.com")


def test_passes_email_long():
    with pytest.raises(Exception):
        visitor.create_visitor(123456, "Vasiliy",
                         "parazitxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                         "xxxxxxxxxxxxxxxxxxxxx@gmail.com")


def test_passes_user_book_id_long():
    with pytest.raises(Exception):
        visitor.add_book_id(123457877798789797978779778976)




