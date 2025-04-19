from sqlalchemy import Column, Integer, String, ForeignKey, Date, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Library(Base):
    """Справочник библиотек"""
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True)
    library_modifier = Column(String, nullable=False, comment='Модификатор библиотеки')
    full_name = Column(String, nullable=False, comment='Полное наименование библиотеки')
    address = Column(String, comment='Адрес библиотеки')
    library_status = Column(String, comment='Статус библиотеки')
    settlement_status = Column(String, comment='Статус библиотеки по принадлежности к населенному пункту')
    modernized = Column(String, comment='Модернизирована в рамках НП "Культура" за федеральные средства')
    location = Column(String, comment='Библиотека расположена')
    responsible_position = Column(String, comment='Должность ответственного за заполнение отчета')
    responsible_name = Column(String, comment='ФИО ответственного')
    phone = Column(String, comment='Телефон')
    email = Column(String, comment='Эл. адрес')

class Book(Base):
    """Справочник книг"""
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    isbn = Column(String, unique=True, comment='ISBN')
    title = Column(String, nullable=False, comment='Наименование книги')
    authors = Column(String, comment='Авторы')
    annotation = Column(String, comment='Аннотация')
    series = Column(String, comment='Серия')
    publisher = Column(String, comment='Издатель (наименование)')
    publication_year = Column(Integer, comment='Год издания')
    cover_type = Column(String, comment='Тип обложки (мягкий/твердый)')
    genre = Column(String, comment='Жанр')
    age_restriction_id = Column(Integer, ForeignKey('age_restrictions.id'), comment='ID возрастного ограничения')
    children_book = Column(String, comment='Книга для детей и юношества (до 18 лет)')
    book_type = Column(String, comment='Тип книги')
    
    age_restriction = relationship("AgeRestriction", back_populates="books")

class AgeRestriction(Base):
    """Справочник возрастных ограничений"""
    __tablename__ = 'age_restrictions'

    id = Column(Integer, primary_key=True)
    restriction = Column(String, nullable=False, unique=True, comment='Строка возрастного ограничения')
    
    books = relationship("Book", back_populates="age_restriction")

class Invoice(Base):
    """Справочник товарных накладных"""
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False, comment='Год')
    number = Column(String, nullable=False, comment='Номер товарной накладной')
    
    __table_args__ = (
        UniqueConstraint('year', 'number', name='unique_invoice'),
    ) 