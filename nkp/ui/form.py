from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, \
    QSpinBox, QDoubleSpinBox, QDateEdit, QTableWidget, QPushButton, QHBoxLayout
from PySide6.QtWidgets import QHeaderView

from nkp.common.const import Columns


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Форма ввода данных")
        self.showMaximized()

        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной горизонтальный layout
        main_layout = QVBoxLayout(central_widget)
        fill_layout = QHBoxLayout(central_widget)

        # Левая часть - форма ввода
        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)

        # Создаем поля для ввода
        self.fields = {}

        # Субъект РФ
        self.fields['subject'] = QLineEdit()
        form_layout.addRow("Субъект РФ:", self.fields['subject'])

        # Модификатор библиотеки
        self.fields['library_modifier'] = QLineEdit()
        form_layout.addRow("Модификатор библиотеки:", self.fields['library_modifier'])

        # Полное наименование библиотеки
        self.fields['library_name'] = QLineEdit()
        form_layout.addRow("Полное наименование библиотеки:", self.fields['library_name'])

        # Адрес библиотеки
        self.fields['address'] = QLineEdit()
        form_layout.addRow("Адрес библиотеки:", self.fields['address'])

        # Статус библиотеки
        self.fields['library_status'] = QComboBox()
        self.fields['library_status'].addItems(["Муниципальная", "Государственная", "Частная"])
        form_layout.addRow("Статус библиотеки:", self.fields['library_status'])

        # Статус библиотеки по принадлежности к населенному пункту
        self.fields['settlement_status'] = QComboBox()
        self.fields['settlement_status'].addItems(["Городская", "Сельская"])
        form_layout.addRow("Статус по населенному пункту:", self.fields['settlement_status'])

        # Модернизирована в рамках НП "Культура"
        self.fields['modernized'] = QComboBox()
        self.fields['modernized'].addItems(["Да", "Нет"])
        form_layout.addRow("Модернизирована в рамках НП \"Культура\":", self.fields['modernized'])

        # Библиотека расположена
        self.fields['location'] = QLineEdit()
        form_layout.addRow("Библиотека расположена:", self.fields['location'])

        # Должность ответственного
        self.fields['responsible_position'] = QLineEdit()
        form_layout.addRow("Должность ответственного:", self.fields['responsible_position'])

        # ФИО ответственного
        self.fields['responsible_name'] = QLineEdit()
        form_layout.addRow("ФИО ответственного:", self.fields['responsible_name'])

        # Телефон
        self.fields['phone'] = QLineEdit()
        form_layout.addRow("Телефон:", self.fields['phone'])

        # Эл. адрес
        self.fields['email'] = QLineEdit()
        form_layout.addRow("Эл. адрес:", self.fields['email'])

        # Наименование книги
        self.fields['book_title'] = QLineEdit()
        form_layout.addRow("Наименование книги:", self.fields['book_title'])

        # Авторы
        self.fields['authors'] = QLineEdit()
        form_layout.addRow("Авторы:", self.fields['authors'])

        # Аннотация
        self.fields['annotation'] = QLineEdit()
        form_layout.addRow("Аннотация:", self.fields['annotation'])

        # Серия
        self.fields['series'] = QLineEdit()
        form_layout.addRow("Серия:", self.fields['series'])

        # ISBN
        self.fields['isbn'] = QLineEdit()
        form_layout.addRow("ISBN:", self.fields['isbn'])

        # Издатель
        self.fields['publisher'] = QLineEdit()
        form_layout.addRow("Издатель:", self.fields['publisher'])

        # Год издания
        self.fields['publication_year'] = QSpinBox()
        self.fields['publication_year'].setRange(1900, 2100)
        form_layout.addRow("Год издания:", self.fields['publication_year'])

        # Тип обложки
        self.fields['cover_type'] = QComboBox()
        self.fields['cover_type'].addItems(["Мягкая", "Твёрдая"])
        form_layout.addRow("Тип обложки:", self.fields['cover_type'])

        # Жанр
        self.fields['genre'] = QLineEdit()
        form_layout.addRow("Жанр:", self.fields['genre'])

        # Возрастное ограничение
        self.fields['age_restriction'] = QComboBox()
        self.fields['age_restriction'].addItems(["0+", "6+", "12+", "16+", "18+"])
        form_layout.addRow("Возрастное ограничение:", self.fields['age_restriction'])

        # Книга для детей и юношества
        self.fields['children_book'] = QComboBox()
        self.fields['children_book'].addItems(["Да", "Нет"])
        form_layout.addRow("Книга для детей и юношества:", self.fields['children_book'])

        # Цена
        self.fields['price'] = QDoubleSpinBox()
        self.fields['price'].setRange(0, 1000000)
        self.fields['price'].setDecimals(2)
        form_layout.addRow("Цена:", self.fields['price'])

        # Количество экземпляров
        self.fields['quantity'] = QSpinBox()
        self.fields['quantity'].setRange(1, 1000)
        form_layout.addRow("Количество экземпляров:", self.fields['quantity'])

        # Итого стоимость
        self.fields['total_cost'] = QDoubleSpinBox()
        self.fields['total_cost'].setRange(0, 10000000)
        self.fields['total_cost'].setDecimals(2)
        self.fields['total_cost'].setReadOnly(True)
        form_layout.addRow("Итого стоимость:", self.fields['total_cost'])

        # Дата поступления
        self.fields['receipt_date'] = QDateEdit()
        self.fields['receipt_date'].setCalendarPopup(True)
        self.fields['receipt_date'].setDate(QDate.currentDate())
        form_layout.addRow("Дата поступления:", self.fields['receipt_date'])

        # Номер товарной накладной
        self.fields['invoice_number'] = QLineEdit()
        form_layout.addRow("Номер товарной накладной:", self.fields['invoice_number'])

        # Тип книги
        self.fields['book_type'] = QComboBox()
        self.fields['book_type'].addItems(["Печатная", "Электронная"])
        form_layout.addRow("Тип книги:", self.fields['book_type'])

        # Комментарий
        self.fields['comment'] = QLineEdit()
        form_layout.addRow("Комментарий:", self.fields['comment'])

        # Кнопка добавления записи
        add_button = QPushButton("Добавить запись")
        form_layout.addRow(add_button)

        # Правая часть - таблица
        table_widget = QWidget()
        table_layout = QVBoxLayout(table_widget)

        # Создаем таблицу
        self.table = QTableWidget()
        self.table.setColumnCount(30)
        self.table.setHorizontalHeaderLabels(Columns.get_values())

        # Устанавливаем режим растягивания для таблицы
        # self.table.horizontalHeader().setStretchLastSection(True)
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Режим растягивания

        table_layout.addWidget(self.table)

        # Добавляем виджеты в основной layout
        fill_layout.addWidget(form_widget)

        main_layout.addWidget(table_widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
