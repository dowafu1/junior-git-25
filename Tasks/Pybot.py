import telebot
from telebot import types
bot = telebot.TeleBot('7818862467:AAE_OaiKLw0btfQHf1eOmR9OOcZgDGRq57o')

@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.from_user.id, 'Напиши /start')
    bot.register_next_step_handler(message, get_age) #следующий шаг – функция get_name
def get_age(message):
        keyboard = types.InlineKeyboardMarkup() #наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
        keyboard.add(key_yes) #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Вход строго 18+!\nТебе есть 18 лет?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        ...
        bot.send_message(call.message.chat.id, 'Архив с хентаем: https://t.me/+VTQ6MLsEWx8yNjAy')
    elif call.data == "no":
         ...
bot.polling(none_stop=True, interval=0)