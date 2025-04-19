from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import os
from pathlib import Path

# Путь к файлу базы данных SQLite
DB_PATH = Path(__file__).parent.parent / 'data' / 'library.db'

# Создаем директорию для базы данных, если её нет
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Создаем строку подключения к SQLite
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# Создаем движок базы данных
# check_same_thread=False нужен для SQLite, чтобы разрешить доступ из разных потоков
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=QueuePool,
    connect_args={"check_same_thread": False},
    pool_size=5,  # максимальное количество соединений в пуле
    max_overflow=10  # максимальное количество дополнительных соединений
)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Функция-генератор для получения сессии базы данных.
    Гарантирует закрытие сессии после использования.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 