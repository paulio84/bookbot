import sys

from book_stats import (
    LetterCount,
    count_letters_in_book,
    count_words_in_book,
    sort_letter_counts,
)


def get_book_text(file_path: str) -> str:
    """
    get_book_text takes a file_path parameter as a string, opens and reads the file.
    It returns a string containing the contents of the book.

    :param file_path: The path to a book file. Should be a textfile.
    :type file_path: str
    :return: The contents of the book.
    :rtype: str
    """
    with open(file_path, encoding="utf-8") as file:
        return file.read()


def print_report(
    file_path: str,
    word_count: int,
    sorted_letters: list[LetterCount],
) -> None:
    print("================== BOOKBOT ==================")
    print(f"Reading book from {file_path}...")
    print("---------------------------------------------")
    print(f"Found {word_count} total words")
    print("---------------------------------------------")
    print("Character counts (by frequency):")
    for item in sorted_letters:
        print(f"{item['char']}: {item['num']}")
    print("==================== END ====================")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    try:
        book_text = get_book_text(file_path)
        if not book_text.strip():
            raise ValueError("The book file is empty")
    except FileNotFoundError:
        print(f"Cannot find the book you are looking for: {file_path}")
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)

    word_count = count_words_in_book(book_text)
    letter_counts = count_letters_in_book(book_text)
    sorted_letters = sort_letter_counts(letter_counts)

    print_report(file_path, word_count, sorted_letters)


if __name__ == "__main__":
    main()
