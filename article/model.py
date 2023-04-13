import pickle
import os.path


class Film:
    def __init__(self, title, genre, page, description):
        self.title = title
        self.genre = genre
        self.page = page
        self.description = description

    def __str__(self):
        return f"{self.title} ({self.author})"

class ArticleModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.articles = self.load_data()

    def add_articles(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_article(self):
        return self.films.values()

    def get_single_article(self, user_title):
        film = self.films[user_title]
        dict_film = {
            "название фильма": film.title,
            "жанр": film.genre,
            "режиссёр": film.director,
            "год выпуска": film.year,
            "длительность": film.length,
            "студия": film.studio
            "актёрский состав": film.cast
        }

        return dict_film

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.films, f)

