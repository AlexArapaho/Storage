import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    res = requests.get(url)
    return res.text


def write_csv(data):
    with open('bookstore.csv', 'a', newline='') as f:
        write = csv.writer(f, delimiter=";", lineterminator="\r")
        write.writerow(data)


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    menu = soup.find("ul", class_="menu").find_all("a", class_="menu-link")
    print("Пункты меню книжного магазина: ")
    for i in menu:
        print(i.text.strip())
        write_csv(i)


def main():
    url = "https://piotrovsky.store/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
