from lib.db.session import Session
from lib.db.models import Car, Customer, Rental
from tabulate import tabulate
from datetime import datetime
from lib.db.session import Session
from lib.db.models import Car, Customer, Rental
def register():
    session = Session()

    username = input("Enter username: ")
    password = input("Enter password: ")

    new_customer = Customer(username=username, password=password)
    session.add(new_customer)
    session.commit()

    print(f"Registration successful! Welcome, {username}")
    session.close()



def login(username, password):
    session = Session()
    customer = session.query(Customer).filter_by(username=username, password=password).first()
    session.close()
    if customer:
        print(f"Welcome back, {username} (ID: {customer.id})!")
    else:
        print("Invalid username or password.")

def browse_cars():
    session = Session()
    cars = session.query(Car).filter_by(available=True).all()
    session.close()

    if not cars:
        print("\n No cars available right now.\n")
        return

    table = [[car.id, car.make, car.model, car.year] for car in cars]
    headers = ["ID", "Make", "Model", "Year"]

    print("\n=== Available Cars ===")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    print()

def rent_car(customer_id):
    car_id = int(input("Enter the Car ID you want to rent: "))
    car = Session.query(Car).get(car_id)

    if car and car.available:
        rental = Rental(car_id=car.id, customer_id=customer_id)
        car.available = False
        Session.add(rental)
        Session.commit()

        # Showing tuple
        rental_tuple = (rental.id, car.make, car.model)
        print("Car rented successfully! Rental record (id, make, model):", rental_tuple)
    else:
        print("Car not available.")


def return_car(rental_id):
    session = Session()
    rental = session.query(Rental).filter_by(id=rental_id, return_date=None).first()
    if not rental:
        print(" Rental not found or already returned.")
    else:
        rental.return_date = datetime.now()
        rental.car.available = True
        session.commit()
        print(f" Car {rental.car.make} {rental.car.model} returned successfully!")
    session.close()

def view_history():
    session = Session()

    try:
        customer_id = int(input("Enter your Customer ID: "))

        rentals = (
            session.query(Rental)
            .filter_by(customer_id=customer_id)
            .all()
        )

        if not rentals:
            print(" No rental history found for this customer.")
        else:
            table_data = []
            for rental in rentals:
                car = rental.car 
                table_data.append([
                    car.make,
                    car.model,
                    car.year,
                    str(rental.rental_date),
                    str(rental.return_date) if rental.return_date else "Not returned yet"
                ])

            headers = ["Make", "Model", "Year", "Rental Date", "Return Date"]
            print("\n Rental History:")
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

    except ValueError:
        print(" Invalid input! Please enter a valid numeric Customer ID.")

    finally:
        session.close()