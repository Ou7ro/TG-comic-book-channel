from environs import env
from bot_utils import send_comics
from comics_handler import (
    get_random_comics_url,
    download_comics,
    delete_comics
)
from telegram.error import TelegramError
from requests import RequestException


def main():
    env.read_env()

    url = get_random_comics_url()
    env.read_env()
    file_name = 'comics.png'
    tg_bot_token = env.str('TG_TOKEN_BOT')
    tg_channel_id = env.str('TG_CHANNEL_ID')
    try:
        download_comics(url, file_name)
        send_comics(tg_bot_token, file_name, tg_channel_id)
    except (RequestException, FileNotFoundError) as e:
        print(f'Ошибка при работе с комиксом: {e}')
    except TelegramError as e:
        print(f'Ошибка со стороны Telegram: {e}')
    finally:
        try:
            delete_comics(file_name)
        except (FileNotFoundError, PermissionError) as e:
            print(f'Ошибка при удалении файла: {e}')


if __name__ == '__main__':
    main()
