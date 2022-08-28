from telebot import TeleBot
from telebot.types import Message, CallbackQuery

from configs import *
from keyboards import *

bot = TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def welcome(message: Message):
    chat_id = message.chat.id
    name = message.from_user.full_name
    bot.send_message(chat_id, f'🍟 Здравствуйте <b>{name}</b>! Я бот для доставки <b>фаст-фуда</b>, выберите с чего мы начнем:',
                     reply_markup=generate_main_menu())


# -------------------------------------------------------------------------------------------------
# Меню
@bot.message_handler(func=lambda message: '🍽 Меню' == message.text)
def categories_menu(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, '📃 Выберите одну из <b>категорий:</b>', reply_markup=generate_categories_menu())
    bot.register_next_step_handler(msg, send_products)

def send_products(message: Message):
    chat_id = message.chat.id
    category_name = message.text

    database = sqlite3.connect('fastfood.db')
    cursor = database.cursor()

    cursor.execute('''
SELECT image FROM categories
WHERE category_name = ?
    ''', (category_name, ))
    category_photo = cursor.fetchone()[0]
    with open(category_photo, mode='rb') as img:
        bot.send_photo(chat_id, photo=img, reply_markup=generate_products_menu(category_name))
# -------------------------------------------------------------------------------------------------
# Мои заказы


# -------------------------------------------------------------------------------------------------
# Оставить отзыв




bot.polling(none_stop=True)
