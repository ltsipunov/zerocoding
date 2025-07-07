import asyncio
from aiogram import Bot,Dispatcher,F

from aiogram.filters import Command,CommandStart
from aiogram.types import Message
import aiohttp

import os
from  dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')
APIKEY = os.getenv('OPENWEATHERMAP_APIKEY')

bot = Bot(token=TOKEN)
dp = Dispatcher()

# -------------------- REQUEST
async def get_weather(city = 'Moscow' ):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}&units=metric"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return None

#---------------------------- HANDLERS ----------------
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!")

@dp.message(Command('help'))
async def help(message):
    await message.answer("""
Этот бот понимает команды /start, /help, /weather 
        """)

@dp.message(Command('weather'))
async def weather(message):
    json= await get_weather()
    await message.answer(f"""
{ json['weather'][0]['description'] }. Температура #{json['main']['temp']}
        """)

@dp.message(F.text == 'Что такое ИИ?')
async def aitext(message):
    await message.answer("""
Искусственный интеллект — это свойство искусственных интеллектуальных систем 
выполнять творческие функции, которые традиционно считаются прерогативой человека; 
наука и технология создания интеллектуальных машин,особенно интеллектуальных компьютерных программ 
         """)

# --------------------------- MAIN  -------------------
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
     asyncio.run(main())