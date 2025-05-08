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

# class Vehicle:
#     def __init__(self, Company, Model, Year):
#         self.Company = Company
#         self.Model = Model 
#         self.Year = Year 

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.Company} is {capacity} passengers"
    
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)
# School_Bus = Bus("Tata", "Marcopolo", 2022)
# print(School_Bus.seating_capacity())

## 5.  Define a property that must have the same value for every class instance (object)

# class Vehicle:

#     color = "White"

#     def __init__(self, Company, Model, Year):
#         self.Company = Company
#         self.Model = Model 
#         self.Year = Year 

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass
# School_Bus = Bus("Tata", "Marcopolo", 2022)
# print("Color:", School_Bus.color, "Company:", School_Bus.Company, "Model:", School_Bus.Model, "Year:", School_Bus.Year )

# Car = Car("BYD", "ATTO3", 2024)
# print("Color:", Car.color, "Company:", Car.Company, "Model:", Car.Model, "Year:", Car.Year)


## 6. Create a Bus child class that inherits from the Vehicle class. The default fare charge for any vehicle is its seating capacity multiplied by 100 

# class Vehicle: 
#     def __init__(self, Company, Model, Year, Capacity):
#         self.Company = Company
#         self.Model = Model 
#         self.Year = Year 
#         self.capacity = Capacity

#     def fare(self):
#         return self.capacity * 100 

# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10 / 100
#         return amount
    
# School_Bus = Bus("Tata", "Marcopolo", 2022, 50)
# print("Total Bus Fare is:", School_Bus.fare())

## 7. Check Type of an Object 
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)

# print(type(School_bus))

## 8. To check for subclass 

class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass
 
print(issubclass(Dog, Animal))
print(issubclass(Puppy, Dog))
print(issubclass(Cat, Animal))
print(issubclass(Puppy, Animal))

