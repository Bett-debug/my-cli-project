from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Car, Customer, Rental
from lib.db.session import engine
import datetime

# Create tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#my mock data
customers = [
    Customer(username="sam", password="2534"),
    Customer(username="jane", password="1234"),
    Customer(username="mike", password="pass")
]


cars = [
    Car(make="Toyota", model="Corolla", year=2020, available=True),
    Car(make="Honda", model="Civic", year=2019, available=True),
    Car(make="Ford", model="Mustang", year=2021, available=True)
]


rentals = [
    Rental(
        customer_id=1,
        car_id=1,
        rental_date=datetime.date(2025, 8, 20), 
        return_date=datetime.date(2025, 9, 23)     
    )
]

session.add_all(customers)
session.add_all(cars)
session.add_all(rentals)

session.commit()
print("Mock data inserted successfully!")
