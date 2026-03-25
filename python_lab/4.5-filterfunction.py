#!/usr/bin/env python
# coding: utf-8

# ##### The filter() Function in Python
# The filter() function constructs an iterator from elements of an iterable for which a function returns true. It is used to filter out items from a list (or any other iterable) based on a condition.

# In[1]:


def even(num):
    if num%2==0:
        return True


# In[2]:


even(24)


# In[3]:


lst=[1,2,3,4,5,6,7,8,9,10,11,12]

list(filter(even,lst))


# In[4]:


## filter with a Lambda Function
numbers=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,numbers))
print(greater_than_five)


# In[5]:


## Filter with a lambda function and multiple conditions
numbers=[1,2,3,4,5,6,7,8,9]
even_and_greater_than_five=list(filter(lambda x:x>5 and x%2==0,numbers))
print(even_and_greater_than_five)


# In[6]:


## Filter() to check if the age is greate than 25 in dictionaries
people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33},
    {'name':'John','age':25}
]

def age_greater_than_25(person):
    return person['age']>25

list(filter(age_greater_than_25,people))


# ##### Conclusion
# The filter() function is a powerful tool for creating iterators that filter items out of an iterable based on a function. It is commonly used for data cleaning, filtering objects, and removing unwanted elements from lists. By mastering filter(), you can write more concise and efficient code for processing and manipulating collections in Python.

# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




