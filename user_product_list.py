import sys
import pyodbc
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QWidget, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize

from app.sql_user import DataBase

class ProductApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Продуктовый интерфейс")
        self.setGeometry(100, 100, 800, 600)
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes;user=22200322;Database=DB_for_python_lessons;'

        # Основной виджет и макет
        self.db = DataBase(conn_str)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Список товаров
        self.product_list = QListWidget()
        self.product_list.setIconSize(QSize(100, 100))  # Размер иконки
        self.layout.addWidget(self.product_list)
        self.load_products()

    def load_products(self):
        # Запрос для получения данных

        for row in self.db.get_info():
            name, price, count, path = row
            print(name, price, count)

            # Создание элемента списка
            item = QListWidgetItem(f"{name}\nЦена: {price} руб.\nКоличество: {count}")
            pixmap = QPixmap(path).scaled(100, 100)  # Подгрузка изображения
            icon = QIcon(pixmap)
            item.setIcon(icon)

            self.product_list.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductApp()
    window.show()
    sys.exit(app.exec_())