# Книжные новинки со страниц книжного магазина (6 страниц)
# в файл загружаются название книги, автор, цена

import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        for i in range(1, 7):
            pag = f'{self.url}{i}'
            req = requests.get(pag).text
            self.html = BeautifulSoup(req, 'lxml')
            self.parsing()

    def parsing(self):
        novelties = self.html.find_all("article", class_="product-card js-product-card")
        for item in novelties:
            i = 0
            title = item.find('a', class_="product-card__title js-product-name").text.strip()
            try:
                author = item.find('div', class_="product-card__categories with-commas").find('a', class_="link").text.strip()
            except AttributeError:
                author = None
            try:
                price = item.find('div', class_="product-card__footer").find('div', class_="product-card__price with-ruble").text.strip()
            except AttributeError:
                price = None
            self.res.append({
                'title': title,
                'author': author,
                'price': price
            })

    def run(self):
        self.get_html()
        self.save()

    def save(self):
        with open(self.path, 'a') as f:
            for item in self.res:
                f.write(f"Название: {item['title']}\nАвтор: {item['author']}\nЦена: {item['price']}"
                        f"\n\n{'*' * 40}\n")


pars = Parser('https://piotrovsky.store/catalog/books/filter/novelty/?&PAGEN_1=', 'novelties.txt')
pars.run()

