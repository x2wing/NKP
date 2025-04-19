from .database import engine, get_db, SessionLocal
from .models import Base, Library, Book, AgeRestriction, Invoice

# Функция для инициализации базы данных
def init_db():
    """
    Создает все таблицы в базе данных.
    Если таблицы уже существуют, они не будут пересозданы.
    """
    Base.metadata.create_all(bind=engine)

# Функция для пересоздания базы данных
def recreate_db():
    """
    Удаляет все таблицы и создает их заново.
    ВНИМАНИЕ: Все данные будут потеряны!
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine) 