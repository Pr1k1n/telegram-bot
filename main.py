import telebot
from telebot import types # для указание типов
import time

bot = telebot.TeleBot("5368896848:AAFDMxKsrqHMtiEExQmVelxaD0ydbrp8Y2M")  # token to access from BotFather 


# message data arrays
# vision = ['- операторов', '- государственных компаний', '- корпоративных клиентов', '- иностранных компаний']

values= ['- Клиентоориентированность', '- Ответственность', '- Профессионализм', '- Инновационность', '- Персонал']

certificates = ['https://www.jusanmobile.kz/public/newcerts/9001.png', 'https://www.jusanmobile.kz/public/img/license/ct-pk-iso-9001-2016-ru.png', 'https://www.jusanmobile.kz/public/newcerts/1401.png']


# to open txt files and encode them
with open('about.txt', 'r', encoding='utf-8') as f:
    about = f.read()

with open('story.txt', 'r', encoding='utf-8') as f:
    story = f.read()


# start command /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # created buttons
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    
    # add buttons to markup
    markup.add(btn1, btn2)

    # sending sticker and message
    bot.send_sticker(message.chat.id, sticker="CAACAgQAAxkBAAMHYnYknSga6dhCdj7sciLoZWiUDOkAAnoFAAJLae4QGrBab3lPMR0kBA".format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я информационный бот AOLF 'KazTransCom'".format(message.from_user), reply_markup=markup)


# read replies (buttons)
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет!")
        bot.send_message(message.chat.id, about)

    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("МИССИЯ")
        # btn2 = types.KeyboardButton("ВИДЕНИЕ")
        btn3 = types.KeyboardButton("ЦЕННОСТИ")
        btn4 = types.KeyboardButton("НАША ИСТОРИЯ")
        btn5 = types.KeyboardButton("СЕРТИФИКАТЫ")
        btn6 = types.KeyboardButton("ПАРТНЕРЫ")

        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn3, btn4, btn5, btn6, back)

        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "МИССИЯ"):
        bot.send_message(message.chat.id, text = "Наша главная миссия это 'Предоставить лучший персональный сервис каждому клиенту на рынке телекоммуникаций'")

    elif(message.text == "ВИДЕНИЕ"):
        bot.send_message(message.chat.id, text="Быть приоритетным провайдером услуг для:")

        # run through array
        for i in range(len(vision)):
            bot.send_message(message.chat.id, vision[i])

    elif(message.text == "ЦЕННОСТИ"):
        bot.send_message(message.chat.id, text="Нашими ценностями являются: ")

        for i in range(len(values)):
            bot.send_message(message.chat.id, values[i])

    elif(message.text == "НАША ИСТОРИЯ"):
        bot.send_message(message.chat.id, text="История создания Компании")

        # data from txt file
        bot.send_message(message.chat.id, story)

    elif(message.text == "СЕРТИФИКАТЫ"):
        bot.send_message(message.chat.id, text="Имеем все необходимые сертификаты международного образца")

        for i in range(len(certificates)):
            bot.send_photo(message.chat.id, certificates[i])


    elif(message.text == "ПАРТНЕРЫ"):
        markup2 = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton('china telecom', url = 'https://www.chinatelecomglobal.com/')
        btn2 = types.InlineKeyboardButton('kazsatnet', url = 'http://www.kazsat.com/')
        btn3 = types.InlineKeyboardButton('Telia Company', url = 'https://www.teliacompany.com/')
        btn4 = types.InlineKeyboardButton('МегаФон', url = 'https://moscow.megafon.ru/#')
        btn5 = types.InlineKeyboardButton('Кыргызтелеком', url = 'https://kt.kg/')
        btn6 = types.InlineKeyboardButton('transtelecom', url = 'https://ttc.kz/ru/')

        markup2.add(btn1, btn2, btn3, btn4, btn5, btn6)

        bot.send_message(message.chat.id, text="НАШИ ПАРТНЕРЫ".format(message.from_user), reply_markup = markup2)

        # bot.send_message(message.chat.id, text="По подробнее можешь узнать на нашем сайте".format(message.from_user), reply_markup=markup1)


    elif (message.text == "Вернуться в главное меню"):
        # reply keyboard button
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        # inline keyboard button
        markup1 = types.InlineKeyboardMarkup()

        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")

        button3 = types.InlineKeyboardButton("Наш сайт", url='https://www.jusanmobile.kz/ru/about')

        markup.add(button1, button2)
        markup1.add(button3)

        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        
        bot.send_message(message.chat.id, text="По подробнее можешь узнать на нашем сайте".format(message.from_user), reply_markup=markup1)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

#bot.polling(none_stop=True)
while True:
    try:
        bot.polling(none_stop=True, timeout=1000)
    except Exception as ex:
        print(ex)
        time.sleep(10)