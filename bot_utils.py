import telegram


def send_comics(tg_token, file_name, tg_channel_id):
    """ Отправка комикса в канал

    Args:
        tg_token (str): токен для работы бота
        path (str): путь откуда берется файл
        tg_channel_id (str): id канала куда отправляется комикс
    """
    bot = telegram.Bot(token=tg_token)
    with open(file_name, 'rb') as save_file:
        bot.send_document(chat_id=tg_channel_id, document=save_file)