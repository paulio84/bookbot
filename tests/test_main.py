import pytest

from main import get_book_text


def test_get_book_test_returns_content_for_populated_file(populated_book_path):
    assert get_book_text(populated_book_path) == "It was a dark and stormy night."


def test_get_book_text_returns_empty_for_empty_file(empty_book_path):
    with pytest.raises(ValueError):
        get_book_text(empty_book_path)


def test_get_book_text_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        get_book_text("path/to/non_existent_file.txt")
