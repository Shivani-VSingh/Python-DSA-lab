#!/usr/bin/env python
# coding: utf-8

# #### Tuples
# Video Outline:
# 1. Introduction to Tuples
# 2. Creating Tuples
# 3. Accessing Tuple Elements
# 4. Tuple Operations
# 5. Immutable Nature of Tuples
# 6. Tuple Methods
# 7. Packing and Unpacking Tuples
# 8. Nested Tuples
# 9. Practical Examples and Common Errors
# 

# 
# ##### Introduction to Tuples
# Explanation:
# 
# Tuples are ordered collections of items that are immutable.
# They are similar to lists, but their immutability makes them different.
# 

# In[1]:


## creating a tuple
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))


# In[2]:


lst=list()
print(type(lst))
tpl=tuple()
print(type(tpl))


# In[3]:


numbers=tuple([1,2,3,4,5,6])
numbers


# In[4]:


list((1,2,3,4,5,6))


# In[5]:


mixed_tuple=(1,"Hello World",3.14, True)
print(mixed_tuple)


# In[6]:


## Accessing Tuple Elements

numbers


# In[9]:


print(numbers[2])
print(numbers[-1])


# In[10]:


numbers[0:4]


# In[12]:


numbers[::-1]


# In[15]:


## Tuple Operations

concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple)


# In[16]:


mixed_tuple * 3


# In[17]:


numbers *3


# In[20]:


## Immutable Nature Of Tuples
## Tuples are immutable, meaning their elements cannot be changed once assigned.

lst=[1,2,3,4,5]
print(lst)

lst[1]="Krish"
print(lst)


# In[23]:


numbers[1]="Krish"


# In[26]:


numbers


# In[27]:


## Tuple Methods
print(numbers.count(1))
print(numbers.index(3))


# In[28]:


## Packing and Unpacking tuple
## packing
packed_tuple=1,"Hello",3.14
print(packed_tuple)


# In[29]:


##unpacking a tuple
a,b,c=packed_tuple

print(a)
print(b)
print(c)


# In[30]:


## Unpacking with *
numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(first)
print(middle)
print(last)


# In[33]:


## Nested Tuple
## Nested List
lst=[[1,2,3,4],[6,7,8,9],[1,"Hello",3.14,"c"]]
lst[0][0:3]


# In[34]:


lst=[[1,2,3,4],[6,7,8,9],(1,"Hello",3.14,"c")]
lst[2][0:3]


# In[36]:


nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))

## access the elements inside a tuple
print(nested_tuple[0])
print(nested_tuple[1][2])


# In[37]:


## iterating over nested tuples
#nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item,end=" ")
    print()


# #### Conclusion
# Tuples are versatile and useful in many real-world scenarios where an immutable and ordered collection of items is required. They are commonly used in data structures, function arguments and return values, and as dictionary keys. Understanding how to leverage tuples effectively can improve the efficiency and readability of your Python code.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




