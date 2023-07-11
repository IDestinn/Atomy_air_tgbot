import asyncio
import logging

from aiogram import Bot, Dispatcher
from tg_bot.config import load_config
from tg_bot.handlers.back import register_back
from tg_bot.handlers.dock_download import register_dock_download
from tg_bot.handlers.navigation import register_navigation
from tg_bot.handlers.welcome import register_welcome


logger = logging.getLogger(__name__)


def register_all_handlers(dp):
    register_welcome(dp)
    register_navigation(dp)
    register_back(dp)
    register_dock_download(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )

    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    #storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage
    dp = Dispatcher(bot)

    bot['config'] = config

    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
