#!/usr/bin/env python
# coding: utf-8

# ##### Standard Library Overview
# Python's Standard Library is a vast collection of modules and packages that come bundled with Python, providing a wide range of functionalities out of the box. Here's an overview of some of the most commonly used modules and packages in the Python Standard Library.

# In[1]:


import array
arr=array.array('i',[1,2,3,4])
print(arr)


# In[2]:


import math
print(math.sqrt(16))
print(math.pi)


# In[6]:


## random 

import random
print(random.randint(1,10))
print(random.choice(['apple','banana','cherry']))


# In[7]:


### File And Directory Access

import os
print(os.getcwd())


# In[8]:


os.mkdir('test_dir')


# In[9]:


## High level operations on files and collection of files
import shutil
shutil.copyfile('source.txt','destination.txt')


# In[10]:


## Data Serialization
import json
data={'name':'Krish','age':25}

json_str=json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data=json.loads(json_str)
print(parsed_data)
print(type(parsed_data))


# In[11]:


## csv

import csv

with open('example.csv',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['Krish',32])

with open('example.csv',mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


# In[12]:


## datetime
from datetime import datetime,timedelta

now=datetime.now()
print(now)

yesterday=now-timedelta(days=1)

print(yesterday)


# In[13]:


## time
import time
print(time.time())
time.sleep(2)
print(time.time())


# In[15]:


## Regular expresiion
import re

pattern=r'\d+'
text='There are 123 apples 456'
match=re.search(pattern,text)
print(match.group())


# #### Conclusion
# Python's Standard Library is extensive and provides tools for almost any task you can think of, from file handling to web services, from data serialization to concurrent execution. Familiarizing yourself with the modules and packages available in the Standard Library can significantly enhance your ability to write efficient and effective Python programs.

# In[ ]:




