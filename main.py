import telegram
from environs import Env

import asyncio
import random
import time
import argparse

from fetch_data_xkcd import fetch_comix
from fetch_data_xkcd import get_comix_count


async def post_comix_in_channel(time_sleep, chat_id_tg, token_bot_tg):
    bot = telegram.Bot(token=token_bot_tg)
    while (True):
        comix_count = get_comix_count()
        comix_indexies = list(range(1, comix_count+1))
        random.shuffle(comix_indexies)
        for comix_index in comix_indexies:
            img_url, comment = fetch_comix(comix_index)
            async with bot:
                await bot.send_photo(
                    chat_id=chat_id_tg,
                    photo=img_url,
                    caption=comment
                )
            time.sleep(time_sleep)
        print(f'All images has been posted into {chat_id_tg}')
        print('Reshuffle images and start posting images again...')


if __name__ == '__main__':
    env = Env()
    env.read_env()
    chat_id_tg = env.str('TELEGRAM_CHAT_ID')
    token_bot_tg = env.str('TELEGRAM_BOT_TOKEN')
    parser = argparse.ArgumentParser(
        description='Post images in telegram channel')
    parser.add_argument(
        'time_sleep',
        help='sleep time in seconds',
        nargs='?',
        type=int,
        default=14400
    )
    parser = parser.parse_args()
    time_sleep = parser.time_sleep
    asyncio.run(post_comix_in_channel(time_sleep, chat_id_tg, token_bot_tg))
