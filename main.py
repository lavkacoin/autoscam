import telebot
from telebot import types
import config
import requests

bot = telebot.TeleBot(config.TOKEN)
HEADERS_ROCKET = {'Rocket-Pay-Key' : config.ROCKET_TOKEN}

#Скам через Tonkeeper

def process_amount_step_tonkeeper(message):
            try:
                amount = int(message.text)
                link = f"https://app.tonkeeper.com/transfer/EQAHbfM0HD19bzOi-KTDIr5wwvmOYPBeIrnFmJ-6gvbBcCeI?amount={amount*1000000000}"
                bot.send_message(chat_id=message.chat.id, text=link)
            except ValueError:
                bot.send_message(chat_id=message.chat.id, text="Неправильное число")

#Скам через Tonhub

def process_amount_step_tonhub(message):
            try:
                amount = int(message.text)
                link = f"https://tonhub.com/transfer/EQAHbfM0HD19bzOi-KTDIr5wwvmOYPBeIrnFmJ-6gvbBcCeI?amount={amount*1000000000}"
                bot.send_message(chat_id=message.chat.id, text=link)
            except ValueError:
                bot.send_message(chat_id=message.chat.id, text="Неправильное число")

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)

    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    #Русский язык
    if message.text == '🇷🇺 Русский':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("💰 ЗАСКАМИТЬСЯ")
        btn2 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.row(btn1)
        markup.row(btn2)
        bot.send_message(message.from_user.id, 'Добро пожаловать в LAVKA autoscam. \n \n LAVKA autoscam это открытая технология для скама. Если раньше вам приходилось покупать сомнительные NFT чтобы заскамиться, ждать скамеров - теперь вы можете просто нажать кнопку ниже. \n \n А так же можете посмотреть открытый исходный код этой технологии + подписаться на LAVKA Foundation \n \n [Канал](https://t.me/lavkaton) | [Сайт](lavkafoundation.fun) | [GitHub](https://github.com/orgs/lavkacoin/repositories) ', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔙 Вернуться к выбору языка':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn1 = types.KeyboardButton("🇷🇺 Русский")
         btn2 = types.KeyboardButton('🇬🇧 English')
         markup.add(btn1, btn2)

         bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text == '💰 ЗАСКАМИТЬСЯ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("💎 Tonkeeper")
        btn2 = types.KeyboardButton('💎 Tonhub')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        bot.send_message(message.from_user.id, 'Через что будем скамиться?', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '💎 Tonkeeper':
        bot.send_message(chat_id=message.chat.id, text="На сколько TON хотите заскамиться?")
        bot.register_next_step_handler(message, process_amount_step_tonkeeper)

    elif message.text == '💎 Tonhub':
        bot.send_message(chat_id=message.chat.id, text="На сколько TON хотите заскамиться?")
        bot.register_next_step_handler(message, process_amount_step_tonhub)
        
#английский язык
    if message.text == '🇬🇧 English':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("💰 GET SCAMMED")
        btn2 = types.KeyboardButton('🔙 Back to language select')
        markup.row(btn1)
        markup.row(btn2)
        bot.send_message(message.from_user.id, 'Welcome to LAVKA autoscam! \n \n LAVKA autoscam is an open-source scam utility. Before LAVKA autoscam. you had to wait for a scam NFT collection or for a scammer to reach you. Now you can just press the button below and get scammed. \n \n Also you can have a look at LAVKA autoscam GitHub and subscribe to LAVKA Foundation \n \n [Channel](https://t.me/lavkaton) | [Website](lavkafoundation.fun) | [GitHub](https://github.com/orgs/lavkacoin/repositories) ', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔙 Back to language select':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn1 = types.KeyboardButton("🇷🇺 Русский")
         btn2 = types.KeyboardButton('🇬🇧 English')
         markup.add(btn1, btn2)

         bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text == '💰 GET SCAMMED':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("💎 Tonkeeper!")
        btn2 = types.KeyboardButton('💎 Tonhub!')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        bot.send_message(message.from_user.id, 'How would you like to get scammed?', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '💎 Tonkeeper!':
        bot.send_message(chat_id=message.chat.id, text="How much would you like to get scammed for?")
        bot.register_next_step_handler(message, process_amount_step_tonkeeper)

    elif message.text == '💎 Tonhub!':
        bot.send_message(chat_id=message.chat.id, text="How much would you like to get scammed for?")
        bot.register_next_step_handler(message, process_amount_step_tonhub)

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
