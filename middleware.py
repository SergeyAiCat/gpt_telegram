from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Any, Awaitable, Callable, Dict
from openai_api import OpenaiApi
from db_posg import DbPosg

class GptMiddleware(BaseMiddleware,OpenaiApi,DbPosg):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        prompt=event.text#текст сообщения пользователя
        oa_answer=await self.gpt_chat(prompt)#ответ от openai
        data['oa_answer'] = oa_answer#добавление ответа от openai в переменную для роутера
        await self.add_request(event.from_user.id,"gpt",prompt, oa_answer)#добавление запроса в базу данных PosgreSQL
        return await handler(event, data)
    
class DalMiddleware(BaseMiddleware,OpenaiApi,DbPosg):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        prompt=event.text
        oa_answer=await self.dal_chat(prompt)
        data['oa_answer'] = oa_answer
        await self.add_request(event.from_user.id,"dal",prompt,oa_answer)
        return await handler(event, data)
    
