import requests
from random import randint
from pathlib import Path


def get_random_comics_url():
    """ Генерация url для случайного комикса

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
    comics_metadata = response.json()

    comics_url = comics_metadata.get('img')
    response = requests.get(comics_url)

    with open(file_name, 'wb') as file:
        file.write(response.content)


def delete_comics(file_name):
    """ Удаление комикса с директории

    Args:
        file_name (str): название файла
    """
    path = Path(file_name)
    if path.is_file():
        path.unlink()
