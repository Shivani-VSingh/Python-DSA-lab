#!/usr/bin/env python
# coding: utf-8

# ### Iterators
# Iterators are advanced Python concepts that allow for efficient looping and memory management. Iterators provide a way to access elements of a collection sequentially without exposing the underlying structure.
# 

# In[6]:


my_list=[1,2,3,4,5,6]
for i in my_list:
    print(i)


# In[7]:


type(my_list)


# In[8]:


print(my_list)


# In[9]:


## Iterator
iterator=iter(my_list)
print(type(iterator))


# In[10]:


iterator


# In[17]:


## Iterate through all the element

next(iterator)


# In[18]:


iterator=iter(my_list)


# In[25]:


try:
    print(next(iterator))
except StopIteration:
    print("There are no elements in the iterator")


# In[26]:


# String iterator
my_string = "Hello"
string_iterator = iter(my_string)

print(next(string_iterator))  # Output: H
print(next(string_iterator))  # Output: e


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




