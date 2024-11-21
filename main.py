from services import *


def main_menu():
    library = load_library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            book = add_book(library, title, author, year)
            print(f"Книга '{book.title}' добавлена в библиотеку.")
            save_library(library)

        elif choice == "2":
            try:
                id_to_delete = int(input("Введите ID книги для удаления: "))
                delete_book(library, id_to_delete)
                print(f"Книга с ID {id_to_delete} удалена.")
                save_library(library)
            except ValueError as e:
                print(e)

        elif choice == "3":
            query = str(input("Введите запрос для поиска: "))
            choice_param_find = input("По какому полю искать? \n1)Название\n2)Автор\n3)Год выпуска\n> ")

            if choice_param_find == "1":
                field = "title"
            elif choice_param_find == "2":
                field = "author"
            elif choice_param_find == "3":
                field = "year"
            else:
                print("Неизвестный параметр")
                continue
            results = search_books(library, query, field)
            if not results:
                print("Книг, соответствующих запросу, не найдено.")
            else:
                display_books(results)

        elif choice == "4":
            display_books(library.books)

        elif choice == "5":
            try:
                id_to_change = int(input("Введите ID книги для изменения статуса: "))
                new_status = input("Введите новый статус ('в наличии'/'выдана'): ")
                change_status(library, id_to_change, new_status)
                print(f"Статус книги с ID {id_to_change} изменен на '{new_status}'.")
                save_library(library)
            except ValueError as e:
                print(e)

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main_menu()
