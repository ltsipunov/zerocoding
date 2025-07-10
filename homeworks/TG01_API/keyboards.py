from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет!"),KeyboardButton(text="Пока!")]
],resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [
    InlineKeyboardButton(text="Восход",   url='https://pxhere.com/ru/photo/1369327'),
    InlineKeyboardButton(text="Полдень",  url='https://pxhere.com/ru/photo/548068'),
    InlineKeyboardButton(text="Закат",    url='https://pxhere.com/ru/photo/105304'),
    InlineKeyboardButton(text="Полночь",  url='https://pxhere.com/ru/photo/855683'),]
   ])

inline_keyboard_extend = InlineKeyboardMarkup(inline_keyboard=[
      [ InlineKeyboardButton(text="Показать больше...", callback_data='extend'),]
   ])

inline_keyboard_options = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вариант 1", callback_data='option1'),
     InlineKeyboardButton(text="Вариант 2", callback_data='option2'),]
   ])

