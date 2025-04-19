from datetime import datetime
from .database import SessionLocal
from .models import Library, Book, AgeRestriction, Invoice

def fill_age_restrictions(db):
    """Заполнение справочника возрастных ограничений"""
    age_restrictions = ["0+","6+", "12+"]
    
    for restriction in age_restrictions:
        existing = db.query(AgeRestriction).filter_by(restriction=restriction).first()
        if not existing:
            age_restriction = AgeRestriction(restriction=restriction)
            db.add(age_restriction)
    
    db.commit()

def fill_libraries(db):
    """Заполнение справочника библиотек"""
    libraries_data = [
        {
            "library_modifier": "70099",
            "full_name": "Детская библиотека №48 (филиал №17) Муниципального бюджетного учреждения Централизованная система детских библиотек городского округа город Уфа Республики Башкортостан",
            "address": "450078, Башкортостан Респ, г Уфа, 8 Марта ул, д. 26",
            "library_status": "Муниципальная",
            "settlement_status": "Городская",
            "modernized": "Нет",
            "location": "",
            "responsible_position": "заведующий ОКиО",
            "responsible_name": "Солуянова Любовь Павловна",
            "phone": "8(917)432-66-14",
            "email": "complcsdb@gmail.com"
        }
    ]
    
    for lib_data in libraries_data:
        existing = db.query(Library).filter_by(library_modifier=lib_data["library_modifier"]).first()
        if not existing:
            library = Library(**lib_data)
            db.add(library)
    
    db.commit()

def fill_invoices(db):
    """Заполнение справочника товарных накладных"""
    invoices_data = [
        {
            "year": 2024,
            "number": "273"
        }
    ]
    
    for inv_data in invoices_data:
        existing = db.query(Invoice).filter_by(year=inv_data["year"], number=inv_data["number"]).first()
        if not existing:
            invoice = Invoice(**inv_data)
            db.add(invoice)
    
    db.commit()

def fill_books(db):
    """Заполнение справочника книг"""
    # Получаем ID возрастного ограничения
    age_restriction = db.query(AgeRestriction).filter_by(restriction="0+").first()
    
    books_data = [
        {
            "isbn": "978-5-389-21621-1",
            "title": "Транквилла Неуклюжевна, или Сказка о черепахе, которая приняла твёрдое решение",
            "authors": "Энде Михаэль",
            "annotation": "",
            "series": "",
            "publisher": "Махаон",
            "publication_year": 2022,
            "cover_type": "Твёрдая обложка",
            "genre": "Художественная литература",
            "age_restriction_id": age_restriction.id if age_restriction else None,
            "children_book": "Да",
            "book_type": "Печатная"
        }
    ]
    
    for book_data in books_data:
        existing = db.query(Book).filter_by(isbn=book_data["isbn"]).first()
        if not existing:
            book = Book(**book_data)
            db.add(book)
    
    db.commit()

def fill_initial_data():
    """Заполнение базы данных начальными данными"""
    db = SessionLocal()
    try:
        fill_age_restrictions(db)
        fill_libraries(db)
        fill_invoices(db)
        fill_books(db)
    finally:
        db.close()

if __name__ == "__main__":
    fill_initial_data() 