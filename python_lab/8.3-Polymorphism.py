#!/usr/bin/env python
# coding: utf-8

# #### Polymorphism
# Polymorphism is a core concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It provides a way to perform a single action in different forms. Polymorphism is typically achieved through method overriding and interfaces

# In[ ]:


class BankAccount:
....def init(self, name, money):
........self.name = name
........self.balance = money

....def deposit(self, amount):
........self.balance = self.balance + amount
........return self.balance

....def withdraw(self, amount):
........if amount > self.balance:
............return "No Money"
........self.balance = self.balance - amount
........return self.balance

....def transfer(self, other_person, amount):
........if amount > self.balance:
............return "Transfer Failed"
........self.withdraw(amount)
........other_person.deposit(amount)
........return "Transfer Worked"

# --- STARTING THE PROGRAM ---
acc1 = BankAccount("John", 1000)
acc2 = BankAccount("Jane", 2000)

# --- RUNNING ACTIONS ---
acc1.deposit(500)
acc1.transfer(acc2, 200)

# --- PRINTING RESULTS ---
print(acc1.name, "Balance:", acc1.balance)
print(acc2.name, "Balance:", acc2.balance)


# In[ ]:


class BankAccount: 
    def init(self, account_holder, initial_balance): 
        self.account_holder = account_holder; 
        self.balance = initial_balance; 
        
    def deposit(self, amount): 
        self.balance = self.balance + amount; 
        return self.balance; 
        
    def withdraw(self, amount): 
        if amount > self.balance: 
            return "Insufficient"; 

        self.balance = self.balance - amount; 
        return self.balance; 
            
    def transfer(self, target, amount): 
        if amount > self.balance: 
            return "Failed"; 
            
        self.withdraw(amount); 
        target.deposit(amount); 
        return "Success"


# ###  Method Overriding
# Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class.

# In[3]:


## Base Class
class Animal:
    def speak(self):
        return "Sound of the animal"
    
## Derived Class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
## Derived class
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
## Function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())
    
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)


# In[5]:


### Polymorphissm with Functions and MEthods
## base class
class Shape:
    def area(self):
        return "The area of the figure"
    
## Derived class 1
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height
    
##DErived class 2

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius *self.radius
    
## Fucntion that demonstrates polymorphism

def print_area(shape):
    print(f"the area is {shape.area()}")


rectangle=Rectangle(4,5)
circle=Circle(3)

print_area(rectangle)
print_area(circle)





# #### Polymorphism with Abstract Base Classes
# Abstract Base Classes (ABCs) are used to define common methods for a group of related objects. They can enforce that derived classes implement particular methods, promoting consistency across different implementations.

# In[6]:


from abc import ABC,abstractmethod

## Define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

## Derived class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car enginer started"
    
## Derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle enginer started"
    
# Function that demonstrates polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())

## create objects of cAr and Motorcycle

car = Car()
motorcycle = Motorcycle()

start_vehicle(car)




# #### Conclusion
# Polymorphism is a powerful feature of OOP that allows for flexibility and integration in code design. It enables a single function to handle objects of different classes, each with its own implementation of a method. By understanding and applying polymorphism, you can create more extensible and maintainable object-oriented programs.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




