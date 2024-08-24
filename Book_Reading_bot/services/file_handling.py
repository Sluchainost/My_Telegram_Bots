import os
import sys


BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    date = text[start: start+size]
    symbols = ',.!:;?'
    if date[-1] in symbols and len(date) <= size and date[-2] not in symbols:
        return date, len(date)
    else:
        if date[-1] in symbols and date[-2] in symbols:
            return _get_part_text(date, 0, size-2)
        return _get_part_text(date, 0, size-1)


def prepare_book(path: str) -> None:
    num = 0
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    while len(text) != 0:
        data = _get_part_text(text, 0, PAGE_SIZE)
        book.setdefault(num+1, data[0].lstrip())
        num += 1
        text = text[len(data[0])+1:]


prepare_book(os.path.join(
    sys.path[0],
    os.path.normpath(BOOK_PATH)
))
