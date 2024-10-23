import sqlite3

def create_db(db_file):
    connec = None
    try:
        connec = sqlite3.connect(db_file)
        print('Connected to database')
    except sqlite3.Error as error:
        print(f"Error connecting to database: {error}")
    return connec

def create_table(connect, sql):
    try:
        cursor = connect.cursor()
        cursor.execute(sql)
        connect.commit()
        print('Table created successfully')
    except sqlite3.Error as error:
        print(f"Error creating table: {error}")

sq_to_products = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

db_name = 'hw.db'
my_connect = create_db(db_name)
if my_connect:
    create_table(my_connect, sq_to_products)


def add_sample_products():
    products = [
        ('Мыло жидкое с запахом ванили', 100.50, 10),
        ('Мыло детское', 80.00, 20),
        ('Шампунь', 150.00, 15),
        ('Гель для душа', 120.00, 5),
        ('Крем для рук', 200.00, 7),
        ('Зубная паста', 50.00, 30),
        ('Дезодорант', 90.00, 12),
        ('Лосьон для тела', 220.00, 6),
        ('Бальзам для губ', 40.00, 25),
        ('Скраб для тела', 180.00, 4),
        ('Маска для лица', 160.00, 3),
        ('Тоник для лица', 70.00, 14),
        ('Соль для ванн', 110.00, 8),
        ('Масло для массажа', 250.00, 2),
        ('Парфюм', 300.00, 1),
        ('Губная помада', 150.00, 9)
    ]
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()
    print('Sample products added successfully')


def update_quantity(product_id, quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (quantity, product_id))
    conn.commit()
    conn.close()
    print(f'Updated quantity for product id {product_id}')


def update_price(product_id, price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (price, product_id))
    conn.commit()
    conn.close()
    print(f'Updated price for product id {product_id}')


def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()
    print(f'Deleted product id {product_id}')


def print_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)
    conn.close()


def print_cheap_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (100, 5))
    products = cursor.fetchall()
    for product in products:
        print(product)
    conn.close()


def search_products_by_title(search_term):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + search_term + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)
    conn.close()


if __name__ == '__main__':
    if my_connect:
        add_sample_products()
        print_all_products()

        print("\nОбновляем количество товара с id = 1:")
        update_quantity(1, 15)
        print_all_products()

        print("\nОбновляем цену товара с id = 2:")
        update_price(2, 85.00)
        print_all_products()

        print("\nУдаляем товар с id = 3:")
        delete_product(3)
        print_all_products()

        print("\nТовары дешевле 100 сом и с количеством больше 5:")
        print_cheap_products()

        print("\nПоиск товаров по слову 'мыло':")
        search_products_by_title('мыло')

