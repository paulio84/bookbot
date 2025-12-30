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


def main():
    file_path = "books/treasureisland.txt"
    book_text = get_book_text(file_path)
    print(book_text)


if __name__ == "__main__":
    main()
