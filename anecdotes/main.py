import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import handlers
import exceptions
from config import Config, load_config

# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
storage = MemoryStorage()

# Загружаем конфиг в переменную config
config: Config = load_config()

# Регестрируем диспетчер
dp = Dispatcher(storage=storage)

# Регистриуем роутеры на диспетчере для основного бота
dp.include_router(handlers.base_router)
dp.include_router(exceptions.exception_router)


async def main() -> None:
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
