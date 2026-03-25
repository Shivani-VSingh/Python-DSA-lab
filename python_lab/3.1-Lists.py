#!/usr/bin/env python
# coding: utf-8

# #### Introduction To Lists
# - Lists are ordered, mutable collections of items.
# - They can contain items of different data types.

# ##### Video Outline:
# 1. Introduction to Lists
# 2. Creating Lists
# 3. Accessing List Elements
# 4. Modifying List Elements
# 5. List Methods
# 6. Slicing Lists
# 7. Iterating Over Lists
# 8. List Comprehensions
# 9. Nested Lists
# 10. Practical Examples and Common Errors

# In[1]:


lst=[]
print(type(lst))


# In[3]:


names=["Krish","Jack","Jacob",1,2,3,4,5]
print(names)


# In[4]:


mixed_list=[1,"Hello",3.14,True]
print(mixed_list)


# In[5]:


### Accessing List Elements

fruits=["apple","banana","cherry","kiwi","gauva"]


# In[9]:


print(fruits[0])
print(fruits[2])
print(fruits[4])
print(fruits[-1])


# In[16]:


print(fruits[1:])
print(fruits[1:3])


# In[17]:


## Modifying The List elements
fruits


# In[19]:


fruits[1]="watermelon"
print(fruits)


# In[21]:


fruits[1:]="watermelon"


# In[22]:


fruits


# In[23]:


fruits=["apple","banana","cherry","kiwi","gauva"]


# In[24]:


## List Methods

fruits.append("orange") ## Add an item to the end
print(fruits)


# In[26]:


fruits.insert(1,"watermelon")
print(fruits)


# In[27]:


fruits.remove("banana") ## Removing the first occurance of an item
print(fruits)


# In[28]:


## Remove and return the last element
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)


# In[29]:


index=fruits.index("cherry")
print(index)


# In[30]:


fruits.insert(2,"banana")
print(fruits.count("banana"))


# In[31]:


fruits


# In[32]:


fruits.sort() ## SSorts the list in ascending order


# In[33]:


fruits


# In[34]:


fruits.reverse() ## REverse the list


# In[35]:


fruits


# In[36]:


fruits.clear() ## Remove all items from the list

print(fruits)


# In[37]:


## Slicing List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])


# In[41]:


numbers[::3]


# In[42]:


numbers[::-2]


# In[44]:


### Iterating Over List

for number in numbers:
    print(number)


# In[45]:


## Iterating with index
for index,number in enumerate(numbers):
    print(index,number)


# In[46]:


## List comprehension
lst=[]
for x in range(10):
    lst.append(x**2)

print(lst)


# In[48]:


[x**2 for x in range(10)]


# ##### List Comprehension
# 
# Basics Syantax            [expression for item in iterable]
# 
# with conditional logic    [expression for item in iterable if condition]
# 
# Nested List Comprehension [expression for item1 in iterable1 for item2 in iterable2]
# 
# 
# 

# In[49]:


### Basic List Comphrension

sqaure=[num**2 for num in range(10)]
print(sqaure)


# In[50]:


### List Comprehension with Condition
lst=[]
for i in range(10):
    if i%2==0:
        lst.append(i)

print(lst)
        


# In[51]:


even_numbers=[num for num in range(10) if num%2==0]
print(even_numbers)


# In[53]:


## Nested List Comphrension

lst1=[1,2,3,4]
lst2=['a','b','c','d']

pair=[[i,j] for i in lst1 for j in lst2]

print(pair)


# In[54]:


## List Comprehension with function calls
words = ["hello", "world", "python", "list", "comprehension"]
lengths = [len(word) for word in words]
print(lengths)  # Output: [5, 5, 6, 4, 13]



# #### Conclusion
# List comprehensions are a powerful and concise way to create lists in Python. They are syntactically compact and can replace more verbose looping constructs. Understanding the syntax of list comprehensions will help you write cleaner and more efficient Python code.

# In[ ]:




