def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title}".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_title("Ввод данных")
    def wait_user_answer(self):
        print("Действия по фильмам: ")
        print("1 - добавление фильма\n"
              "2 - каталог фильмов\n"
              "3 - просмотр определённого фильма\n"
              "4 - удаление фильма\n"
              "q - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Добавление фильма")
    def add_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссёр": None,
            "год выхода": None,
            "длительность": None,
            "студия": None,
            "актёрский состав": None
        }
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        return dict_film

    @add_title("Каталог фильмов")
    def catalogue(self, films):
        if len(films) == 0:
            print(f"Каталог пуст".center(50))
        else:
            for ind, film in enumerate(films, start=1):
                print(f"{ind}.{film}")


    @add_title("Ввод названия фильма")
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film

    @add_title("Просмотр фильма")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} - {film[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_error(self, user_title):
        print(f"Фильм с названием {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_film(self, film):
        print(f"Фильм {film} - был удален")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")

