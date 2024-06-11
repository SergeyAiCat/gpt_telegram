from aiogram import Router
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from markup import MyCallback
from fsm_state import ai_model
#объявление callback роутера
my_callback = Router()
#Устанавливаем фильтр, который при выборе модели и нажатии соответсвующей кнопки, установит состояние ожидания сообщения.
@my_callback.callback_query(MyCallback.filter(F.callback == "gpt3"))
async def gpt4_callback(query: CallbackQuery, state: FSMContext):
    await query.message.answer("🤖: Приветствую, я чат GPT-3.5 Turbo.\nПишите свои вопросы и задачи, отправляйте голосовые сообщения.✍️")
    return await state.set_state(ai_model.gpt3)


@my_callback.callback_query(MyCallback.filter(F.callback == "dal2"))
async def gpt4_callback(query: CallbackQuery, state: FSMContext):
    await query.message.answer("🤖: Создание картинок DALL·E 2.\nОпишите изображение, которое хотите увидеть.✍️")
    return await state.set_state(ai_model.dal2)
    