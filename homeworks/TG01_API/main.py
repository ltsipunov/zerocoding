import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery
import aiohttp

from googletrans import Translator
from gtts import gTTS
import keyboards as kb

import os
from  dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')
APIKEY = os.getenv('OPENWEATHERMAP_APIKEY')

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()
# -------------------- REQUESTS ------------------------
async def get_weather(city = 'Moscow' ):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}&units=metric&lang=ru"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return None

async def translate(text):
    try:
        # Определение языка автоматически
        detected_lang = await translator.detect(text)
        dest = ['en','ru'][detected_lang.lang == 'en']
        translated = await translator.translate(text, dest=dest)
        # translated = await translator.translate(text, dest= 'en')
        return translated.text
    except Exception as e:
        return f"Sorry..: {e}"

#---------------------------- HANDLERS ----------------
@dp.message(CommandStart())
async def start(message: Message):
    # await message.answer("Добрый день, с вами общается бот-недоучка!")
    await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.main)

@dp.message(Command('help'))
async def help(message):
    await message.answer("""
Я - бот, понимаю команды /start, /help, /weather, /links
Любой нераспознанный  текст переводится с русского на английский  и с английского на русский.  
        """)

@dp.message(Command('links'))
async def links(message):
    await message.answer(f"Покажу красивые картинки 24/7 !", reply_markup=kb.inline_keyboard_test)

@dp.message(Command('dynamic'))
async def dynamic(message):
    await message.answer(f"Динамическое меню", reply_markup=kb.inline_keyboard_extend)

# ---------------------------- BUTTON HANDLERS -------------------------------
@dp.message(F.text=='Привет!')
async def hello_responder(message):
    await message.answer(f"Привет, {message.from_user.first_name} !")

@dp.message(F.text=='Пока!')
async def bye_responder(message):
    await message.answer(f"До свидания, {message.from_user.first_name} !")

@dp.callback_query(F.data=='extend')
async def proceed_responder(callback):
    await callback.message.edit_text(f"Динамическое меню !",reply_markup=kb.inline_keyboard_options)

@dp.callback_query(F.data=='option1')
async def proceed_responder(callback):
    await callback.answer("Выбрал")
    await callback.message.answer(f"Выбран вариант 1")

@dp.callback_query(F.data=='option2')
async def proceed_responder(callback):
    await callback.message.answer(f"Выбран вариант 2")


# ---------------------------- WEATHER HANDLER -------------------------------
@dp.message(Command('weather'))
async def weather(message):
    winddir = lambda d: ['Севврный','Северо-Восточный','Восточный','Юго-Восточный',
                         'Южный', 'Юго-Западный','Западный','Северо-Западный',][ round(d/45) ]
    city = 'Moscow'
    json= await get_weather(city)
    text=f"""
Прогноз погоды на сегодня для города {json['name']}    
Температура {int( json['main']['temp'] )} градусов ощущается как {int( json['main']['temp'] )} градусов. 
{ json['weather'][0]['description'] }, влажность {json['main']['humidity'] }  процентов   
Ветер { winddir(json['wind']['deg']) }, скорость { int(json['wind']['speed']) } метров в секунду
        """
    await message.answer(text+"\nПодождите, для тех, кто не понял, сейчас зачитаю текст....")
    tts =  gTTS(text=text, lang='ru')
    tts.save("temp.ogg")
    audio = FSInputFile("temp.ogg")
    await bot.send_voice(chat_id=message.chat.id, voice=audio)
    os.remove("temp.ogg")

@dp.message(F.text == 'Что такое ИИ?')
async def aitext(message):
    await message.answer("""
Искусственный интеллект — это свойство искусственных интеллектуальных систем 
выполнять творческие функции, которые традиционно считаются прерогативой человека; 
наука и технология создания интеллектуальных машин,особенно интеллектуальных компьютерных программ 
         """)

@dp.message(F.photo)
async def react_photo(message: Message):
    await message.answer('Принимаю фото...')
    await bot.download(message.photo[-1],destination=f'img/{message.photo[-1].file_id}.png')

@dp.message()
async def default(message):
    trs = await translate(message.text)
    await message.answer(trs)

# --------------------------- MAIN  -------------------
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
     asyncio.run(main())