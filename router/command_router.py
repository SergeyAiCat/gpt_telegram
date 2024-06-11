from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from markup import markup
#объявление экземпляра класса для инлайн клавиатуры
mrk=markup()
##объявление command роутера
my_command = Router()
#при нажатии start отправляет привественное сообщение
@my_command.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"🤖: Привет, {message.from_user.full_name}\n выберите нейросеть", reply_markup=await mrk.ai_grid())
