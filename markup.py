from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class MyCallback(CallbackData, prefix="my"):
    callback: str
#создание инлайн клавиатуры с помощью билдера    
class markup: 
    async def ai_grid(self):
        self.builder=InlineKeyboardBuilder()
        self.builder.button(text='💬GPT-3.5 TURBO', callback_data=MyCallback(callback="gpt3").pack())
        self.builder.button(text='🌆DALLE 2', callback_data=MyCallback(callback="dal2").pack())
        self.builder.adjust(2)
        return self.builder.as_markup()
