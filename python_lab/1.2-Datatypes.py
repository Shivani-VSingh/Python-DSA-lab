#!/usr/bin/env python
# coding: utf-8

# ## DataTypes
# #### 1. Definition:
# 
# - Data types are a classification of data which tell the compiler or interpreter how the programmer intends to use the data.
# - They determine the type of operations that can be performed on the data, the values that the data can take, and the amount of memory needed to store the data.
# 
# #### 2. Importance of Data Types in Programming
# Explanation:
# 
# - Data types ensure that data is stored in an efficient way.
# - They help in performing correct operations on data.
# - Proper use of data types can prevent errors and bugs in the program.

# Video Outline:
# 1. Introduction to Data Types
# 2. Importance of Data Types in Programming
# 3. Basic Data Types
#    - Integers
#    - Floating-point numbers
#    - Strings
#    - Booleans
# 4. Advanced Data Types
#    - Lists
#    - Tuples
#    - Sets
#    - Dictionaries
# 5. Type Conversion
# 6. Practical Examples

# In[1]:


## Integer Example
age=35
type(age)


# In[2]:


##floating point datatype
height=5.11
print(height)
print(type(height))


# In[3]:


## string datatype example
name="Krish"
print(name)
print(type(name))


# In[7]:


## boolean datatype
is_true=True
type(is_true)


# In[11]:


a=10
b=10

type(a==b)


# In[12]:


## common errors

result="Hello" + 5
 


# In[14]:


result="Hello" + str(5)
print(result)


# In[ ]:




