from environs import env
from bot_utils import send_comics
from comics_handler import (
    get_random_comics,
    download_comics,
    delete_comics
)


def main():
    env.read_env()

    url = get_random_comics()
    env.read_env()
    file_name = 'comics.png'
    tg_bot_token = env.str('TG_TOKEN_BOT')
    tg_channel_id = env.str('TG_CHANNEL_ID')
    download_comics(url, file_name)
    send_comics(tg_bot_token, file_name, tg_channel_id)
    delete_comics(file_name)


if __name__ == '__main__':
    main()
