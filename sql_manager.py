import pyodbc

class DataBase:
    def __init__(self, conn_str):
        self.connect = pyodbc.connect(conn_str)
        self.cursor = self.connect.cursor()

    def get_info(self):
        with self.connect:
            return self.cursor.execute("""SELECT * FROM products""").fetchall()

    def add_product(self, product_name, price, count):
        with self.connect:
            return self.cursor.execute("""INSERT INTO products (product_name, price, count) VALUES (?, ?, ?)""", 
            (product_name, price, count))

    def update_product(self, product_id, product_name, price, count):
        with self.connect:
            return self.cursor.execute("""UPDATE products SET product_name=(?), price=(?), count=(?) WHERE product_id=(?)""", (product_name, price, count, product_id))
        
    def delete_user(self, product_id, product_name, price, count):
        with self.connect:
            return self.cursor.execute("""DELETE FROM products WHERE product_id = (?) AND product_name = (?) AND price = (?) AND count = (?)""", 
                                        (product_id, product_name, price, count))