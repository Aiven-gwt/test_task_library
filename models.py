class Book:
    def __init__(self, id: int, title: str, author: str, year: str, status="в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_book_by_id(self, id: int) -> Book | None:
        for book in self.books:
            if book.id == id:
                return book
        return None

    def remove_book(self, id: int):
        book = self.get_book_by_id(id)
        if book is not None:
            self.books.remove(book)
        else:
            raise ValueError(f"Книга с ID {id} не найдена.")

    def find_books(self, query: str, field="title") -> list:
        results = []
        for book in self.books:
            if query.lower() in getattr(book, field).lower():
                results.append(book)
        return results

    def update_book_status(self, id: int, new_status: str):
        book = self.get_book_by_id(id)
        if book is not None:
            book.status = new_status
        else:
            raise ValueError(f"Книга с ID {id} не найдена.")

    def to_json(self) -> list:
        return [book.to_dict() for book in self.books]

    @classmethod
    def from_json(cls, data):
        library = cls()
        for book_data in data:
            book = Book(**book_data)
            library.add_book(book)
        return library
