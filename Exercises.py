#OOP 

## 1. Create a class with instance attributes 
# class Vehicle: 
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage 
# Ferrari = Vehicle(300, 10)
# print(Ferrari.max_speed, Ferrari.mileage)

## 2. Create a vehile class without any variables and methods 

# class Vehicle: 
#     pass 

## 3.  Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

# class Vehicle: 
#     def __init__(self, Company, Model, Year):
#         self.Company = Company
#         self.Model = Model 
#         self.Year = Year 

# class Bus(Vehicle):
#     pass
# School_Bus = Bus("Tata", "Marcopolo", 2022)
# print("Company:", School_Bus.Company, "Model:", School_Bus.Model, "Year:", School_Bus.Year )  


## 4. Class Inheritance:: Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50. 

class Vehicle:
    def __init__(self, Company, Model, Year):
        self.Company = Company
        self.Model = Model 
        self.Year = Year 

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.Company} is {capacity} passengers"
    
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
School_Bus = Bus("Tata", "Marcopolo", 2022)
print(School_Bus.seating_capacity())
#print("Company:", School_Bus.Company, "Model:", School_Bus.Model, "Year:", School_Bus.Year, "Capacity:", School_Bus.capacity ) 



