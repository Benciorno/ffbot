import sqlite3
from telebot.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)


def generate_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_menu = KeyboardButton(text='🍽 Меню')
    btn_myorders = KeyboardButton(text='🛍 Мои заказы')
    btn_feedback = KeyboardButton(text='✍🏻 Оставить отзыв')
    markup.add(btn_menu, btn_myorders, btn_feedback)
    return markup


def generate_categories_menu():
    database = sqlite3.connect('fastfood.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT category_name FROM categories;
    ''')
    categories = cursor.fetchall()
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for category in categories:
        btn = KeyboardButton(text=category[0])
        buttons.append(btn)
    markup.add(*buttons)
    database.close()

    btn_cart = KeyboardButton(text='🛒 Корзина')
    btn_back = KeyboardButton(text='⬅ Назад')
    markup.row(btn_cart, btn_back)

    return markup

def generate_products_menu(category_name):
    database = sqlite3.connect('fastfood.db')
    cursor = database.cursor()
    cursor.execute('''
SELECT product_name FROM categories
JOIN products USING(category_id)
WHERE category_name = ?
    ''', (category_name, ))

    products = cursor.fetchall()

    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for product in products:
        btn = KeyboardButton(text=product[0])
        buttons.append(btn)
    markup.add(*buttons)
    return markup
