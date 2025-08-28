# test_display.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Car, Customer, Rental, Base

# Connect to DB
engine = create_engine("sqlite:///lib/db/rental.db")
Session = sessionmaker(bind=engine)
session = Session()

print(" All Cars in DB:")
for car in session.query(Car).all():
    print(f"{car.id}: {car.make} {car.model} ({car.year}) - ${car.daily_rate}/day - Available: {car.is_available}")

print("\n All Customers in DB:")
for customer in session.query(Customer).all():
    print(f"{customer.id}: {customer.name} ({customer.email})")

print("\n All Rentals in DB:")
for rental in session.query(Rental).all():
    print(f"Rental {rental.id}: {rental.customer.name} -> {rental.car.make} {rental.car.model}, Returned: {rental.returned}")
print("\n Display test completed.")