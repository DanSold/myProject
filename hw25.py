import sqlite3

products = [
    ('Coca-Cola sugar', '250 ml, with sugar', 17.5),
    ('Pepsi', '250 ml, no sugar', 20),
    ('Fanta', '330 ml, no sugar, with juice', 22.2),
    ('Sprite sugar', '1 l, with sugar', 18.9),
    ('Waffles with sugar', '500 g', 33),
    ('Potato', '1 kg', 55),
    ('Tomato', '1 kg', 66),
    ('Pineapples in sugar', '333 g', 100),
    ('Cherry', '1 kg', 80),
    ('Cherry in sugar', '333 kg', 90)
]

with sqlite3.connect('database.db') as connection:
    cursor = connection.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS product(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                description TEXT,
                price FLOAT NOT NULL
            );
    """)

    cursor.executemany(
        """
        INSERT INTO product (name, description, price)
        VALUES (?, ?, ?)
        """,
        products,
    )
