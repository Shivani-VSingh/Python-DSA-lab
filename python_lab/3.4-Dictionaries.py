#!/usr/bin/env python
# coding: utf-8

# #### Dictionaries
# Video Outline:
# 1. Introduction to Dictionaries
# 2. Creating Dictionaries
# 3. Accessing Dictionary Elements
# 4. Modifying Dictionary Elements
# 5. Dictionary Methods
# 6. Iterating Over Dictionaries
# 7. Nested Dictionaries
# 8. Dictionary Comprehensions
# 9. Practical Examples and Common Errors

# ##### Introduction to Dictionaries
# 
# Dictionaries are unordered collections of items. They store data in key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any type.

# In[1]:


## Creating Dictionaries
empty_dict={}
print(type(empty_dict))


# In[2]:


empty_dict=dict()
empty_dict


# In[4]:


student={"name":"Krish","age":32,"grade":24}
print(student)
print(type(student))


# In[5]:


# Single key is slways used
student={"name":"Krish","age":32,"name":24}
print(student)


# In[6]:


## accessing Dictionary Elements
student={"name":"Krish","age":32,"grade":'A'}
print(student)


# In[10]:


## Accessing Dictionary elements
print(student['grade'])
print(student['age'])

## Accessing using get() method
print(student.get('grade'))
print(student.get('last_name'))
print(student.get('last_name',"Not Available"))


# In[11]:


## Modifying Dicitonary Elements
## Dictionary are mutable,so you can add, update or delete elements
print(student)


# In[12]:


student["age"]=33  ##update value for the key
print(student)
student["address"]="India" ## added a new key and value
print(student)


# In[13]:


del student['grade'] ## delete key and value pair

print(student)


# In[14]:


## Dictionary methods

keys=student.keys() ##get all the keys
print(keys)
values=student.values() ##get all values
print(values)

items=student.items() ##get all key value pairs
print(items)


# In[22]:


## shallow copy
student_copy=student
print(student)
print(student_copy)


# In[23]:


student["name"]="Krish2"
print(student)
print(student_copy)


# In[24]:


student_copy1=student.copy() ## shallow copy
print(student_copy1)
print(student)


# In[25]:


student["name"]="KRish3"
print(student_copy1)
print(student)


# In[27]:


### Iterating Over Dictionaries
## You can use loops to iterate over dictionatries, keys,values,or items

## Iterating over keys
for keys in student.keys():
    print(keys)


# In[28]:


## Iterate over values
for value in student.values():
    print(value)


# In[29]:


## Iterate over key value pairs
for key,value in student.items():
    print(f"{key}:{value}")


# In[30]:


## Nested Disctionaries
students={
    "student1":{"name":"Krish","age":32},
    "student2":{"name":"Peter","age":35}
}
print(students)


# In[31]:


## Access nested dictionaries elementss
print(students["student2"]["name"])
print(students["student2"]["age"])


# In[32]:


students.items()


# In[34]:


## Iterating over nested dictionaries
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")


# In[35]:


## Dictionary Comphrehension
squares={x:x**2 for x in range(5)}
print(squares)


# In[36]:


## Condition dictionary comprehension
evens={x:x**2 for x in range(10) if x%2==0}
print(evens)


# In[37]:


## Practical Examples

## USe a dictionary to count he frequency of elements in list

numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)


# In[38]:


## Merge 2 dictionaries into one

dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2}
print(merged_dict)


# #### Conclusion
# Dictionaries are powerful tools in Python for managing key-value pairs. They are used in a variety of real-world scenarios, such as counting word frequency, grouping data, storing configuration settings, managing phonebooks, tracking inventory, and caching results. Understanding how to leverage dictionaries effectively can greatly enhance the efficiency and readability of your code.

# In[ ]:




