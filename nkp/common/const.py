from enum import Enum

class Columns(Enum):
    SUBJECT_RF = "Субъект РФ"
    LIBRARY_MODIFIER = "Модификатор библиотеки" 
    LIBRARY_FULL_NAME = "Полное наименование библиотеки"
    LIBRARY_ADDRESS = "Адрес библиотеки"
    LIBRARY_STATUS = "Cтатус библиотеки"
    LIBRARY_SETTLEMENT_STATUS = "Статус библиотеки по населенному пункту"
    MODERNIZED_IN_NP = 'Модернизирована в рамках НП "Культура"'
    LIBRARY_LOCATION = "Библиотека расположена"
    RESPONSIBLE_POSITION = "Должность ответственного"
    FULL_NAME = "ФИО"
    PHONE = "Телефон"
    EMAIL = "Эл. адрес"
    BOOK_NAME = "Наименование книги"
    AUTHORS = "Авторы"
    ANNOTATION = "Аннотация"
    SERIES = "Серия"
    ISBN = "ISBN"
    PUBLISHER = "Издатель"
    PUBLICATION_YEAR = "Год издания"
    COVER_TYPE = "Тип обложки"
    GENRE = "Жанр"
    AGE_RESTRICTION = "Возрастное ограничение"
    CHILDREN_BOOK = "Книга для детей и юношества"
    PRICE = "Цена"
    COPIES_COUNT = "Кол-во экземпляров"
    TOTAL_COST = "Итого стоимость"
    RECEIPT_DATE = "Дата поступления"
    INVOICE_NUMBER = "Номер товарной накладной"
    BOOK_TYPE = "Тип книги"
    COMMENT = "Комментарий"

    @classmethod
    def get_values(cls):
        return [col.value for col in cls]

if __name__ == '__main__':

    print(Columns.get_values())
