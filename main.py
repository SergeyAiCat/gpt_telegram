import asyncio
import logging
import sys
import redis.asyncio as redis
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from router import *
from config import TOKEN
from aiogram.fsm.storage.redis import RedisStorage
from db_posg import DbPosg
#добавление redis как хранилище состояний
r = redis.Redis(host='redis', port=6379, decode_responses=True)
storage=RedisStorage(redis=r)
#объявление диспатчера и добавление к нему роутеров
dp = Dispatcher(storage=storage)
dp.include_router(my_command)
dp.include_router(my_callback)
dp.include_router(my_gpt)
dp.include_router(my_dal)

async def main():
    db_pg = DbPosg()#объявление экземпляра класса базы данных PostgreSQL
    await db_pg.db_create()#создать таблицу ,если не существует
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)#кофигурация и запуск бота

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())#логирование и точка входа