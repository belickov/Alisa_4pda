import requests
from bs4 import BeautifulSoup


list_link_4pda = {}


def list_link_4pda_fun():
    """
    Функция для сборв заголовков и ссылок
    Заполняет глобальный словарь list_link_4pda
    """
    req = requests.get("https://4pda.to/")
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, "html.parser")
        x = soup.find_all(class_="list-post-title")
        for i in x:
            for y in i:
                if "Обзор" not in y["title"]:
                    list_link_4pda[f'{y["title"]}'] = f"{y['href']}"
                else:
                    pass
    return print("link OK")


def pars_link_4pda(URL: str) -> list:
    """
    Функция получает на вход ссылку на статью которую нужно получить
    отдает список с текстом разбитый по обзацам
    """
    processed_text = []
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, "html.parser")
    try:
        x = soup.find('div', class_="content-box").find_all("p", style="text-align: justify;")
        if len(x) > 1:
            for y in x:
                processed_text.append(y.text)
        x = soup.find('div', class_="content-box").find_all("p", style="text-align:justify")
        if len(x) > 1:
            for y in x:
                processed_text.append(y.text)
        else:
            print("Нет подходящей формы")
    except AttributeError:
        pass
    return processed_text