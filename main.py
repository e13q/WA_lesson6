import telegram
from environs import Env

import asyncio
import random

from fetch_data_xkcd import fetch_comix
from fetch_data_xkcd import get_comix_count


async def post_comix_in_channel(chat_id_tg, token_bot_tg):
    bot = telegram.Bot(token=token_bot_tg)
    comix_count = get_comix_count()
    comix_indexies = list(range(1, comix_count+1))
    comix_index = random.choice(comix_indexies)
    img_url, comment = fetch_comix(comix_index)
    async with bot:
        await bot.send_photo(
            chat_id=chat_id_tg,
            photo=img_url,
            caption=comment
        )


if __name__ == '__main__':
    env = Env()
    env.read_env()
    chat_id_tg = env.str('TELEGRAM_CHAT_ID')
    token_bot_tg = env.str('TELEGRAM_BOT_TOKEN')
    asyncio.run(post_comix_in_channel(chat_id_tg, token_bot_tg))
