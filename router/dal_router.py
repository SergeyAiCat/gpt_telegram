from aiogram import Router
from aiogram.types import Message
from aiogram import F
from fsm_state import ai_model
from middleware import DalMiddleware
#объявление dalle роутера
my_dal = Router()
#добавление middleware c dalle openai api
my_dal.message.middleware(DalMiddleware())
#бот ответит при отправке промта
@my_dal.message(F.text, ai_model.dal2)
async def message_handler(message: Message,oa_answer):
    await message.answer_photo(oa_answer)