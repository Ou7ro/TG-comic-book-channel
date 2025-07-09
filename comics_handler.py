import requests
from random import randint
from pathlib import Path


def get_random_comics():
    """ Генерация случайного номера

    Returns:
        str: url случайного комикса
    """
    last_comics = 3112
    random_number = randint(1, last_comics)
    url = f'https://xkcd.com/{random_number}/info.0.json'
    return url


def download_comics(url, file_name):
    """ Загрузка комикса с сайта

    Args:
        url (str): cсылка на комикс
        comics_path (str): название комикса
    """

    response = requests.get(url)
    response.raise_for_status()
    url_contents = response.json()

    comics_url = url_contents.get('img')
    comics_title = url_contents.get('alt')
    response = requests.get(comics_url)

    with open(file_name, 'wb') as file:
        file.write(response.content)

    print(comics_title)


def delete_comics(file_name):
    """ Удаление комикса с директории

    Args:
        file_name (str): название файла
    """
    try:
        path = Path(file_name)
        if path.is_file():
            path.unlink()
    except FileNotFoundError:
        print('Комикс не найден')
    except PermissionError:
        print('Нет прав на удаление')
