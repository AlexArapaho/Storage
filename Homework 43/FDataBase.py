import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_catalog(self):
        sql = "SELECT * FROM catalog"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res

        except IOError:
            print('Ошибка чтения из БД')
        return []

    def add_item(self, name, description, price):
        try:
            self.__cur.execute('INSERT INTO product_catalog VALUES(NULL, ?, ?, ?)', (name, description, price))
            self.__db.commit()
        except sqlite3.Error as e:
            print(f"Ошибка добавления карточки товара в БД {e}")
            return False
        return True

    def get_items(self):
        try:
            self.__cur.execute(f"SELECT id, name, description, price FROM product_catalog")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print(f"Ошибка получения карточки товара из БД {e}")
        return False, False

    def get_item(self, item_id):
        try:
            self.__cur.execute(f"SELECT id, name, description, price FROM product_catalog WHERE id = {item_id}")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print(f"Ошибка получения статьи из БД  {e}")
        return False, False