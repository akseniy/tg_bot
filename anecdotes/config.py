"""В этом файле мы создаем класс описывающий наши конфигурационные данные и функцию, необходимую для закрузги этих
самых данных"""

from dataclasses import dataclass
from environs import *


@dataclass
class DatabaseConfig:
    database: str         # Название базы данных
    db_host: str          # URL-адрес базы данных
    db_user: str          # Username пользователя базы данных
    db_password: str      # Пароль к базе данных
    db_port: str          # Порт базы данных


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config() -> Config:
    # Создаем экземпляр класса Env
    env: Env = Env()
    # Добавляем в переменные окружения данные, прочитанные из файла .env
    env.read_env()

    # Создаем экземпляр класса Config и наполняем его данными из переменных окружения
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS'))),

        ),
        db=DatabaseConfig(
            database=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD'),
            db_port=env('PORT')
        ))
