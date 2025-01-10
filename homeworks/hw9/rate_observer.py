import telebot
from datetime import datetime as dt ,timedelta as td
from time import sleep
import threading
import requests
import xml.etree.ElementTree as ET
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

bot= telebot.TeleBot('7992697765:AAHZpuW2azSZvpFn18WaoleILsHP4NAp964')
global currencies
currencies='USD JPY'

#  ============================== START & SXHEDULE REQUEST ========================================
def get_latest_rates():
    url = f'https://api.exchangerate-api.com/v4/latest/RUB'
    currencies= 'USD EUR CNY'.split()
    response = requests.get(url)

    if response.status_code == 200:
        rates,data = {},response.json()
        for cur in currencies:
            if cur in data['rates']:
                rates[cur ] = round( 1/data['rates'][cur],4)
        result = f"Курсы к RUB: "+",".join(f'{currency}: {rate}' for currency, rate in rates.items())
    else:
        result = f"Ошибка при получении данных: {response.status_code} "
    print(result)
    return result

def send_request(chat_id):
    while True:
        now=dt.now()
        sleep(30)
        if now.strftime("%M")  in ['00']:
            s = get_latest_rates()
            s = f"{now:%d.%m.%y %H:%M}  {s}"
            sleep(60)
            print(now,s)
            bot.send_message( chat_id, s )

@bot.message_handler(commands=['start'])
def start_message(message):
    global currencies
    print(currencies)
    currencies='EUR CNY'
    print(currencies)
    bot.reply_to(message, 'Привет! Я чат-бот, информирующий о курсах валют \n Введите /help для информации по доступным командам')
    request_thread= threading.Thread( target=send_request, args= [message.chat.id] )
    request_thread.start()

@bot.message_handler(commands=['help'])
def help_message(message):
    rates_help = """
/rates [список валют] 
- Информация о текущих курсах валют к рублю  с exchangerate
  список по умолчанию : USD EUR CNY         
"""
    days_help = """
/days N [список валют] 
- Информация о курсах валют к рублю от Центробанка за N последних дней 
  список по умолчанию : USD EUR CNY         
"""
    bot.reply_to(message, ''.join([rates_help,days_help]) )

@bot.message_handler(commands=['rates'])
def rates_message(message):
    context= message.text.upper().split(' ')
    currencies = "USD EUR CNY".split()
    currencies = context[1:]  if context[1:]  else currencies
    url = f'https://api.exchangerate-api.com/v4/latest/RUB'
    response = requests.get(url)

    if response.status_code == 200:
        rates,data = {},response.json()
        for cur in currencies:
            if cur in data['rates']:
                rates[cur ] = round( 1/data['rates'][cur],4)
        result = f"Курсы к RUB: "+",".join(f'{currency}: {rate}' for currency, rate in rates.items())
    else:
        result = f"Ошибка при получении данных: {response.status_code} "
    print(result)
    bot.reply_to(message,result)

# ========================== HISTORY CENTROBANK ====================================
def get_history_rates(date, currencies):
    url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}'
    print('url=',url )
    response = requests.get(url)
    print("respnse=",response.content)

    if response.status_code == 200:
        # Парсим XML-ответ и создаем словарь для хранения курсов валют
        root,rates  = ET.fromstring(response.content), { }
        # Ищем интересующие нас валюты
        for child in root.findall('Valute'):
            char_code = child.find('CharCode').text
            if char_code in currencies:
                value = child.find('Value').text.replace(',', '.')  # Заменяем запятую на точку
                rates[char_code] = float(value)

        return rates
    else:
        print(f'Ошибка: {response.status_code}')
        return None

@bot.message_handler(commands=['days'])
def days_message(message):
    context= message.text.upper().split(' ')
    currencies = "USD EUR CNY".split()
    currencies= context[2:]  if context[2:]  else currencies
    try:
        days = int(context[1])
    except ValueError:
        message.reply_text("Количество дней должно быть числом.")
        return

    response_message = f"Курсы валют за последние {days} дней:\n"
    response_message+= (" "*8).join(["     Дата      "]+currencies)
    for i in range(days):
        dstr = f"{dt.now() - td(days=i):%d/%m/%Y}"
        rates = get_history_rates( dstr,currencies )
        print("rates=" ,rates)
        if rates:
            response_message+=f"\n{dstr}\t"
            for cur in currencies:
                val= rates.get(cur ,None)
                response_message += f"{val}\t"
        else:
            bot.reply_to(message,"Не удалось получить данные о курсе валют.")
    bot.reply_to(message,response_message)

# ================================= RUN BOT ========================================================
bot.polling(none_stop=True)