#!/usr/bin/env python
# coding: utf-8

# ### Variables
# Variables are fundamental elements in programming used to store data that can be referenced and manipulated in a program. In Python, variables are created when you assign a value to them, and they do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable.
# 
# Video Outline:
# - Introduction to Variables
# - Declaring and Assigning Variables
# - Naming Conventions
# - Understanding Variable Types
# - Type Checking and Conversion
# - Dynamic Typing
# - Practical Examples and Common Errors

# In[1]:


a=100


# In[2]:


## Declaring And Assigning Variables

age=32
height=6.1
name="Krish"
is_student=True

## printing the variables

print("age :",age)
print("Height:",height)
print("Name:",name)


# In[3]:


## Naming Conventions
## Variable names should be descriptive
## They must start with a letter or an '_' and contains letter,numbers and underscores
## variables names case sensitive

#valid variable names

first_name="KRish"
last_name="Naik"


# In[6]:


# Invalid variable names
#2age=30
#first-name="Krish"
##@name="Krish"


# In[7]:


## case sensitivity
name="Krish"
Name="Naik"



# In[10]:


## Understnading Variable types
## Python is dynamically typed,type of a variable is determined at runtime
age=25 #int
height=6.1 #float
name="KRish" #str
is_student=True #bool

print(type(name))


# In[11]:


## Type Checking and Conversion

type(height)


# In[13]:


age=25
print(type(age))

# Type conversion
age_str=str(age)
print(age_str)
print(type(age_str))


# In[15]:


age='25'
print(type(int(age)))


# In[16]:


name="Krish"
int(name)


# In[17]:


height=5.11
type(height)


# In[19]:


float(int(height))


# In[20]:


## Dynamic Typing
## Python allows the type of a vraible to change as the program executes
var=10 #int
print(var,type(var))

var="Hello"
print(var,type(var))

var=3.14
print(var,type(var))



# In[26]:


## input

age=int(input("What is the age"))
print(age,type(age))


# In[27]:


### Simple calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)


# In[ ]:





# In[25]:





# In[ ]:





# ### Conclusion:
# Variables are essential in Python programming for storing and manipulating data. Understanding how to declare, assign, and use variables effectively is crucial for writing functional and efficient code. Following proper naming conventions and understanding variable types will help in maintaining readability and consistency in your code.

# 
