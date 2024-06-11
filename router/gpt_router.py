from aiogram import Router
from aiogram.types import Message
from aiogram import F
from fsm_state import ai_model
from middleware import GptMiddleware
#объявление dalle роутера
my_gpt = Router()
#добавление middleware c dalle openai api
my_gpt.message.middleware(GptMiddleware())
#бот ответит при отправке промта
@my_gpt.message(F.text, ai_model.gpt3)
async def message_handler(message: Message,oa_answer):
    await message.answer(oa_answer)