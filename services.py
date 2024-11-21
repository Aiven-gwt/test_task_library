import json

from models import Library, Book


def load_library(filename="library.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return Library.from_json(data)
    except FileNotFoundError:
        return Library()


def save_library(library: Library, filename="library.json"):
    with open(filename, "w") as file:
        json.dump(library.to_json(), file, indent=4)


def add_book(
        library: Library,
        title: str,
        author: str,
        year: str
) -> Book:
    next_id = max([book.id for book in library.books], default=0) + 1
    book = Book(next_id, title, author, year)
    library.add_book(book)
    return book


def delete_book(library: Library, id_to_delete: int):
    library.remove_book(id_to_delete)


def search_books(library: Library, query: str, field="title"):
    return library.find_books(query, field)


def display_books(books: list):
    for book in books:
        print(f"{book.id} | {book.title} | {book.author} | {book.year} | {book.status}")


def change_status(
        library: Library,
        id_to_change: int,
        new_status: str
) -> None:
    library.update_book_status(id_to_change, new_status)
