#!/usr/bin/env python
# coding: utf-8

# #### Functions in Python
# Video Outline:
# 1. Introduction to Functions
# 2. Defining Functions
# 3. Calling Functions
# 4. Function Parameters
# 5. Default Parameters
# 6. Variable-Length Arguments
# 7. Return Statement

# ##### Introduction to Functions
# Definition:
# 
# A function is a block of code that performs a specific task.
# Functions help in organizing code, reusing code, and improving readability.
# 
# 

# In[1]:


## syntax
def function_name(parameters):
    """Docstring"""
    # Function body
    return expression


# In[2]:


## why functions?
num=24
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")


# In[5]:


def even_or_odd(num):
    """This function finds even or odd"""
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")


# In[6]:


## Call this function
even_or_odd(24)


# In[7]:


## function with multiple parameters

def add(a,b):
    return a+b

result=add(2,4)
print(result)
    


# In[9]:


## Default Parameters

def greet(name):
    print(f"Hello {name} Welcome To the paradise")

greet("Krish")


# In[12]:


def greet(name="Guest"):
    print(f"Hello {name} Welcome To the paradise")

greet("Krish")


# In[13]:


### Variable Length Arguments
## Positional And Keywords arguments

def print_numbers(*krish):
    for number in krish:
        print(number)


# In[14]:


print_numbers(1,2,3,4,5,6,7,8,"Krish")


# In[15]:


## Positional arguments
def print_numbers(*args):
    for number in args:
        print(number)


# In[16]:


print_numbers(1,2,3,4,5,6,7,8,"Krish")


# In[17]:


### Keywords Arguments

def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
#print_details(name="Krish",age="32",country="India")


# In[18]:


print_details(name="Krish",age="32",country="India")


# In[19]:


def print_details(*args,**kwargs):
    for val in args:
        print(f" Positional arument :{val}")
    
    for key,value in kwargs.items():
        print(f"{key}:{value}")


# In[20]:


print_details(1,2,3,4,"Krish",name="Krish",age="32",country="India")


# In[21]:


### Return statements
def multiply(a,b):
    return a*b

multiply(2,3)


# In[22]:


### Return multiple parameters
def multiply(a,b):
    return a*b,a

multiply(2,3)


# In[ ]:




