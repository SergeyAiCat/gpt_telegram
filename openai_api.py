from openai import AsyncOpenAI
import httpx
from config import openai_key

class OpenaiApi:
    client_oa = AsyncOpenAI(
    api_key=openai_key,
    http_client=httpx.AsyncClient(proxy="http://2KQzNJ:2MSj7e@38.170.252.179:9184")
    )#переопределяем httpx клиент, добавляя в него Канадский прокси

    async def gpt_chat(self, prompt):#модель gpt-3.5-turbo
        async with self.client_oa as client:#используем исинхронный with для автоматического закрытия close(openai Github)
            chat_completion = await client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-3.5-turbo",
            )   
        return chat_completion.choices[0].message.content
    
    async def dal_chat(self, prompt):
        async with self.client_oa as client:#модель dall-e-2
            response = await client.images.generate(
            model="dall-e-2",
            prompt= prompt,
            size="1024x1024",
            quality="standard",
            n=1,
            )
            image_url = response.data[0].url
        return image_url

