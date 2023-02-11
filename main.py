import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start']) #стартовая команда
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🇷🇺 Русский", callback_data="ru")
    btn2 = types.InlineKeyboardButton('🇬🇧 English', callback_data="en")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "ru":
        def message_handler(message):
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Заскамиться", callback_data="scam")
            btn2= types.InlineKeyboardButton(text='Канал', url='https://t.me/lavkaton')
            btn3= types.InlineKeyboardButton(text='Сайт', url='https://lavkafoundation.fun')
            btn4= types.InlineKeyboardButton(text='Github', url='https://github.com/lavkacoin/autoscam')
            btn5 = types.InlineKeyboardButton('🔙 Вернуться к выбору языка', callback_data="languageswtich")
            markup.row(btn1)
            markup.row(btn2, btn3)
            markup.row(btn4)
            markup.row(btn5)
            bot.send_message(message.chat.id, "Добро пожаловать в LAVKA autoscam. \n \n LAVKA autoscam это открытая технология для скама. Если раньше вам приходилось покупать сомнительные NFT чтобы заскамиться, ждать скамеров - теперь вы можете просто нажать кнопку ниже. \n \n А так же можете посмотреть открытый исходный код этой технологии + подписаться на LAVKA Foundation", reply_markup=markup)

    elif call.data == "en":
        def message_handler(message):
            bot.send_message(message.chat.id, "Yes/no?")


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть