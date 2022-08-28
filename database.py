import sqlite3

database = sqlite3.connect('fastfood.db')
cursor = database.cursor()


def create_categories_table():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS categories(
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name VARCHAR(50) UNIQUE,
    image TEXT
)''')


# create_categories_table()
def insert_categories():
    cursor.execute('''
INSERT INTO categories(category_name, image)
VALUES ('Сет 🍱', 'photo/categories/Set.jpg'),
       ('Лаваш 🌯', 'photo/categories/Lavash.jpg'),
       ('Шаурма 🌮', 'photo/categories/Shaurma.jpg'),
       ('Донар 🥙', 'photo/categories/Donar.jpg'),
       ('Бургер 🍔', 'photo/categories/Burger.jpg'),
       ('Хот-Дог 🌭', 'photo/categories/Hot-Dog.jpg'),
       ('Десерты 🍰', 'photo/categories/Desert.jpg'),
       ('Напитки 🥤', 'photo/categories/Napitki.jpg'),
       ('Гарнир 🍟', 'photo/categories/Garnir.jpg')
''')


# insert_categories()

def create_products_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        product_name VARCHAR(20) NOT NULL UNIQUE,
        price DECIMAL(12, 2) NOT NULL,
        description VARCHAR(100),
        image TEXT,
        FOREIGN KEY(category_id) REFERENCES categories(category_id)
    )
    ''')


# create_products_table()


def insert_products():
    cursor.execute('''
INSERT INTO products(category_id, product_name, price, description, image)
VALUES
(1,
'COMBO +',
16000,
'Самое выгодное предложение! Горячий хрустящий картофель фри и стакан Pepsi',
'photo/products/Set1.jpg'),
(1,
'Kids COMBO',
16000,
'Выгодное предложение для маленьких гостей за 16 000 сум',
'photo/products/Set2.jpg')
''')


# insert_products()
database.commit()
database.close()
