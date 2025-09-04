from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base



Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)
    color = Column(String, nullable=True)
    

    rentals = relationship("Rental", back_populates="car")

    def __repr__(self):
        return f"<Car(id={self.id}, make={self.make}, model={self.model}, year={self.year}, daily_rate={self.daily_rate}, is_available={self.is_available})>"

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    rentals = relationship("Rental", back_populates="customer")

    def __repr__(self):
        return f"<Customer(username='{self.username}')>"

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    rental_date = Column(DateTime)
    return_date = Column(DateTime)

    car = relationship("Car", back_populates="rentals")
    customer = relationship("Customer", back_populates="rentals")

    def __repr__(self):
        return f"<Rental(id={self.id}, car_id={self.car_id}, customer_id={self.customer_id}, start={self.start_date}, end={self.end_date})>"
    


from lib.db.session import engine
# Base.metadata.create_all(engine)
