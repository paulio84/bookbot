import pytest

from book_stats import (
    LetterCount,
    count_letters_in_book,
    count_words_in_book,
    sort_letter_counts,
)

word_count_test_cases = [
    ("these are four words", 4),
    ("the quick brown fox jumps over the lazy dog.", 9),
    ("", 0),
    ("abcdefghijklmnopqrstuvwxyz", 1),
]


@pytest.mark.parametrize("book_text, word_count", word_count_test_cases)
def test_count_words_in_book(book_text: str, word_count: int):
    assert count_words_in_book(book_text) == word_count


letters_in_book_test_cases = [
    (
        "it was a dark and stormy night.",
        {
            "i": 2,
            "t": 3,
            "w": 1,
            "a": 4,
            "s": 2,
            "d": 2,
            "r": 2,
            "k": 1,
            "n": 2,
            "o": 1,
            "m": 1,
            "y": 1,
            "g": 1,
            "h": 1,
        },
    ),
    (
        "a b c d e f g",
        {
            "a": 1,
            "b": 1,
            "c": 1,
            "d": 1,
            "e": 1,
            "f": 1,
            "g": 1,
        },
    ),
    ("", {}),
]


@pytest.mark.parametrize("book_text, expected", letters_in_book_test_cases)
def test_count_letters_in_book(book_text: str, expected: dict[str, int]):
    assert count_letters_in_book(book_text) == expected


sort_letter_counts_test_cases = [
    (
        {
            "i": 2,
            "t": 3,
            "w": 1,
            "a": 4,
            "s": 2,
            "d": 2,
            "r": 2,
            "k": 1,
            "n": 2,
            "o": 1,
            "m": 1,
            "y": 1,
            "g": 1,
            "h": 1,
        },
        [
            {"char": "a", "num": 4},
            {"char": "t", "num": 3},
            {"char": "d", "num": 2},
            {"char": "i", "num": 2},
            {"char": "n", "num": 2},
            {"char": "r", "num": 2},
            {"char": "s", "num": 2},
            {"char": "g", "num": 1},
            {"char": "h", "num": 1},
            {"char": "k", "num": 1},
            {"char": "m", "num": 1},
            {"char": "o", "num": 1},
            {"char": "w", "num": 1},
            {"char": "y", "num": 1},
        ],
    ),
    ({}, []),
]


@pytest.mark.parametrize("letter_counts, expected", sort_letter_counts_test_cases)
def test_sort_letter_counts(letter_counts: dict[str, int], expected: list[LetterCount]):
    assert sort_letter_counts(letter_counts) == expected
