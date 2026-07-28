# Project 2 – Vehicle Management System
# 
# Features:
# 
# Base Vehicle class.
# Car, Bike, and Bus subclasses.
# Display details.
# Demonstrate inheritance.

class Vehicle:

    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def display_details(self):
        print("Brand :",self.brand)
        print("Model :",self.model)
        print("Year  :",self.year)
        

class Car(Vehicle):
    def __init__(self,brand,model,year,doors):
        super().__init__(brand,model,year)
        self.doors=doors
    
    def display_details(self):
        super().display_details()
        print("Doors :",self.doors,"\n\n")

class Bike(Vehicle):

    def __init__(self,brand,model,year,cc):
        super().__init__(brand,model,year)
        self.cc=cc
    
    def display_details(self):
        super().display_details()
        print("Bike CC is :",self.cc,"\n\n")

class Bus(Vehicle):

    def __init__(self,brand,model,year,seats):
        super().__init__(brand,model,year)
        self.seats=seats

    def display_details(self):
        super().display_details()
        print("No.of Seats are :",self.seats,"\n\n")


car=Car("BMW","X6",2025,4)
bike=Bike("BMW","Z11",2024,200)
bus=Bus("Volvo","Z914",2023,60)

car.display_details()
bike.display_details()
bus.display_details()