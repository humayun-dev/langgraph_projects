from .connection import SessionLocal
from .models import Sales

def seed():

    db = SessionLocal()

    data = [
        Sales(product="Laptop", city="Karachi", quantity=3, price=1200),
        Sales(product="Phone", city="Lahore", quantity=5, price=600),
        Sales(product="Tablet", city="Karachi", quantity=2, price=800),
        Sales(product="Laptop", city="Islamabad", quantity=4, price=1200),
    ]

    db.add_all(data)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()