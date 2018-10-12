import pytest
import visitor

my_visitor = visitor.Visitor.create_visitor(123456, "Vasiliy",
                                            "parazit@gmail.com")


def test_return_visitor():
    """Check return data. If I call create_visitor(1234, "vasil' .....)

    Then class return expected by me data.
    """

    # Create test visitor

    name = my_visitor.name
    email = my_visitor.email
    visitor_id = my_visitor.visitor_id
    my_visitor.add_in_backpack(1234, 5678, 9101112, 7889)
    used_book_id = my_visitor.used_books_id

    # Check return data
    assert name == "Vasiliy"
    assert email == "parazit@gmail.com"
    assert visitor_id == 123456
    assert used_book_id == [1234, 5678, 9101112, 7889]

# If delivered empty.


def test_empty_id():
    with pytest.raises(Exception):
        visitor.Visitor.create_visitor(" ", "dsds", "parazit@gmail.com")


def test_empty_name():
    with pytest.raises(Exception):
        visitor.Visitor.create_visitor(123456, " ", "parazit@gmail.com")


def test_empty_email():
    with pytest.raises(Exception):
        visitor.Visitor.create_visitor(123456, "dsds", " ")


def test_empty_add_in_backpack():
    with pytest.raises(Exception):
        my_visitor.add_in_backpack(" ")


# If delivered short.

def test_id_short():
    with pytest.raises(Exception):
        visitor.Visitor.create_visitor(123, "Vasiliy", "parazit@gmail.com")


def test_name_short():
    with pytest.raises(Exception):
        visitor.Visitor.create_visitor(123456, "Vas", "parazit@gmail.com")


def test_email_short():
    with pytest.raises(Exception):
        visitor.Visitor.create_visitor(123456, "Vasiliy", "p@u.r")


def test_add_in_backpack_short():
    with pytest.raises(Exception):
        my_visitor.add_in_backpack(844)

# If delivered long.


def test_id_long():
    with pytest.raises(Exception):
        visitor.Visitor.create_visitor(123478988567891, "Vasiliy",
                                       "parazit@gmail.com")


def test_name_long():
    with pytest.raises(Exception):
        visitor.Visitor.create_visitor(123456, "Vasiluiiygrtdefrt",
                                       "parazit@gmail.com")


def test_email_long():
    with pytest.raises(Exception):
        visitor.Visitor.create_visitor(123456, "Vasiliy",
                         "parazitxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                         "xxxxxxxxxxxxxxxxxxxxx@gmail.com")


def test_add_in_backpack_long():
    with pytest.raises(Exception):
        my_visitor.add_in_backpack(844345345345345345345354354345345)
