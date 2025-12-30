import pytest


@pytest.fixture
def empty_book_path(tmp_path):
    """Fixture for a book with no content."""
    file = tmp_path / "emptybook.txt"
    file.write_text("")
    return str(file)


@pytest.fixture
def populated_book_path(tmp_path):
    """Fixture for a book with some text."""
    file = tmp_path / "frankenstein.txt"
    file.write_text("It was a dark and stormy night.")
    return str(file)
