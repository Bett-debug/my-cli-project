from lib.helpers import register, login, browse_cars, rent_car, return_car
from lib.db.session import Session
from lib.db.models import Car

    

def main():
    while True:
        print("\n--- Car Rental CLI ---")
        print("1. Register")
        print("2. Login")
        print("3. Browse Cars")
        print("4. Rent Car")
        print("5. Return Car")
        print("6. Add Car")
        print("7. Exit")
        

        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)

        elif choice == "3":
            browse_cars()

        elif choice == "4":
            car_id = int(input("Enter Car ID to rent: "))
            customer_id = int(input("Enter your Customer ID: "))
            rent_car(customer_id, car_id)

        elif choice == "5":
            rental_id = int(input("Enter Rental ID to return: "))
            return_car(rental_id)

        elif choice == "6":
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter year: "))  

            session = Session()
            car = Car(make=make, model=model, year=year, available=1)
            session.add(car)
            session.commit()
            session.close() 

            print(f"Car {make} {model} added successfully!") 
            

        elif choice == "7":
            print("Goodbye!")

            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
