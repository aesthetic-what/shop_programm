import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize
from PyQt5 import uic

from app.sql_user import DataBase

class ProductApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Продуктовый интерфейс")
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes;user=22200322;Database=DB_for_python_lessons;'
        uic.loadUi('design/shop_window.ui', self)
        # Основной виджет и макет
        self.db = DataBase(conn_str)
        # Список товаров
        self.shop_list.setIconSize(QSize(100, 100))  # Размер иконки
        self.load_products()
        self.buy_button.clicked.connect(self.buy_prod)
        self.exit_button.clicked.connect(self.exit)

    def buy_prod(self):
        items = self.shop_list.currentItem().text()
        item_list = items.split(' ')
        processed_item = [int(item) if item.isdigit() else str(item) for item in item_list]
        print(processed_item)

        # print(item_list[3])
        # print(type(item_list[3]))
        # print(int(item_list[3]), type(item_list[3]))
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Подтвердите')
        msg_box.setText('Подтвердие покупку')
        msg_box.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        result = msg_box.exec_()
        if result == QMessageBox.Ok:
            print(processed_item[6])
            processed_item[6] -= 1
            self.db.buy_prod(processed_item[6], processed_item[0])
            print(processed_item[6])
            self.shop_list.editItem(self, items)
            QMessageBox.information(self, 'Успех', 'товар успешно куплен')
        elif result == QMessageBox.Cancel:
            QMessageBox.information(self, 'Отмена', 'Покупка отменена')



    def exit(self):
        pass

    def load_products(self):
        # Запрос для получения данных

        for row in self.db.get_info():
            name, price, count, path = row
            print(name, price, count)

            # Создание элемента списка
            item = QListWidgetItem(f"{name} \n Цена: {price} руб.\n Количество: {count}")
            pixmap = QPixmap(path).scaled(100, 100)  # Подгрузка изображения
            icon = QIcon(pixmap)
            item.setIcon(icon)

            self.shop_list.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductApp()
    window.show()
    sys.exit(app.exec_())