from typing import TypedDict


class LetterCount(TypedDict):
    char: str
    num: int


def count_words_in_book(book_text: str) -> int:
    """
    count_words_in_book takes a string (the book text) and splits it on any whitespace character.
    It returns the number of words in the book.

    :param book_text: The text of the book.
    :type book_text: str
    :return: The number of words in the book.
    :rtype: int
    """
    return len(book_text.split())


def count_letters_in_book(book_text: str) -> dict[str, int]:
    """
    count_letters_in_book counts the number of times each letters occurs in the book.

    :param book_text: The text of the book.
    :type book_text: str
    :return: Returns a dictionary containing the letters as keys
    and the number of occurences as values.
    :rtype: dict[str, int]
    """
    letters = {}
    for character in book_text.lower():
        if character.isalpha():
            letters[character] = letters.get(character, 0) + 1

    return letters


def sort_letter_counts(letter_counts: dict[str, int]) -> list[LetterCount]:
    """
    sort_letter_counts sorts the dictionary of letters by the number of occurences, descending.

    :param letter_counts: A dictionary of the number of occurences of letters.
    :type letter_counts: dict[str, int]
    :return: A sorted list of letters, each as a dictionary item e.g. {"char": "a", "num": 14}
    :rtype: list[LetterCount]
    """
    sorted_letters = [{"char": ch, "num": count} for ch, count in letter_counts.items()]
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters


def sort_on(items: LetterCount) -> int:
    return items["num"]
