#!/usr/bin/env python
# coding: utf-8

# #### Working With File Paths
# When working with files in Python, handling file paths correctly is crucial to ensure your code works across different operating systems and environments. Python provides several modules and functions for working with file paths effectively.

# In[1]:


#### Using the os module
import os
cwd=os.getcwd()
print(f"Current working directory is {cwd}")


# In[5]:


## create a new directory
new_directory="package"
os.mkdir(new_directory)
print(f"Directory '{new_directory}' create")


# In[6]:


## Listing Files And Directories
items=os.listdir('.')
print(items)


# In[7]:


### Joining Paths

dir_name="folder"
file_name="file.txt"
full_path=os.path.join(dir_name,file_name)
print(full_path)


# In[8]:


dir_name="folder"
file_name="file.txt"
full_path=os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)


# In[9]:


path='example1.txt'
if os.path.exists(path):
    print(f"The path '{path}' exists")
else:
    print(f"The path '{path}' does not exists")


# In[10]:


#Checking if a Path is a File or Directory
import os

path = 'example.txt'
if os.path.isfile(path):
    print(f"The path '{path}' is a file.")
elif os.path.isdir(path):
    print(f"The path '{path}' is a directory.")
else:
    print(f"The path '{path}' is neither a file nor a directory.")


# In[11]:


## Getting the absolute path
relative_path='example.txt'
absolute_path=os.path.abspath(relative_path)
print(absolute_path)


# In[ ]:




