#!/usr/bin/env python
# coding: utf-8

# ##### Lambda Functions in Python
# Lambda functions are small anonymous functions defined using the **lambda** keyword. They can have any number of arguments but only one expression. They are commonly used for short operations or as arguments to higher-order functions.
# 
# 

# In[1]:


#Syntax
lambda arguments: expression


# In[2]:


def addition(a,b):
    return a+b


# In[3]:


addition(2,3)


# In[5]:


addition=lambda a,b:a+b
type(addition)
print(addition(5,6))


# In[6]:


def even(num):
    if num%2==0:
        return True
    
even(24)


# In[7]:


even1=lambda num:num%2==0
even1(12)


# In[8]:


def addition(x,y,z):
    return x+y+z

addition(12,13,14)


# In[9]:


addition1=lambda x,y,z:x+y+z
addition1(12,13,14)


# In[10]:


## map()- applies a function to all items in a list
numbers=[1,2,3,4,5,6]
def square(number):
    return number**2

square(2)


# In[12]:


list(map(lambda x:x**2,numbers))


# In[ ]:





# In[ ]:





# In[ ]:




