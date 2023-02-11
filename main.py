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

#Скам через TonRocket

def process_amount_step_rocket(message):
    try:
        amount = int(message.text)
        payload = {
                    "amount": amount,
                    "numPayments": 1,
                    "currency": "TONCOIN",
                    "description": "Pay to get scammed",
                    "hiddenMessage": "thank you",
                    "callbackUrl": "https://t.me/lavkaton",
                    "expiredIn": 300
                }
        response = requests.post("https://pay.ton-rocket.com/tg-invoices", headers=HEADERS_ROCKET, json=payload)
        if response.status_code == 200:
            link = response.json()['link']
            bot.send_message(chat_id=message.chat.id, text=link)
        else:
            bot.send_message(chat_id=message.chat.id, text="Failed to create invoice. Please try again later.")
    except ValueError:
        bot.send_message(chat_id=message.chat.id, text="Invalid amount. Please enter a valid amount.")

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
        btn3 = types.KeyboardButton('🚀 Ton Rocket')
        btn4 = types.KeyboardButton('💎 CryptoBot')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        bot.send_message(message.from_user.id, 'Через что будем скамиться?', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '💎 Tonkeeper':
        bot.send_message(chat_id=message.chat.id, text="На сколько TON хотите заскамиться?")
        bot.register_next_step_handler(message, process_amount_step_tonkeeper)

    elif message.text == '💎 Tonhub':
        bot.send_message(chat_id=message.chat.id, text="На сколько TON хотите заскамиться?")
        bot.register_next_step_handler(message, process_amount_step_tonhub)
    
    elif message.text == '🚀 Ton Rocket':
        bot.send_message(chat_id=message.chat.id, text="На сколько TON хотите заскамиться?")
        bot.register_next_step_handler(message, process_amount_step_rocket)
    
    elif message.text == '💎 CryptoBot':
        bot.send_message(chat_id=message.chat.id, text="На сколько TON хотите заскамиться?")
        bot.register_next_step_handler(message, process_amount_step_rocket)

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
