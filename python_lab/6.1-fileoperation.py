#!/usr/bin/env python
# coding: utf-8

# #### File Operation- Read And Write Files
# 
# File handling is a crucial part of any programming language. Python provides built-in functions and methods to read from and write to files, both text and binary. This lesson will cover the basics of file handling, including reading and writing text files and binary files.

# In[2]:


### Read a Whole File

with open('example.txt','r') as file:
    content=file.read()
    print(content)


# In[6]:


## Read a file line by line
with open('example.txt','r') as file:
    for line in file:
        print(line.strip()) ## sstrip() removes the newline character


# In[7]:


## Writing a file(Overwriting)

with open('example.txt','w') as file:
    file.write('Hello World!\n')
    file.write('this is a new line.')


# In[10]:


## Write a file(wwithout Overwriting)
with open('example.txt','a') as file:
    file.write("Append operation taking place!\n")


# In[11]:


### Writing a list of lines to a file
lines=['First line \n','Second line \n','Third line\n']
with open('example.txt','a') as file:
    file.writelines(lines)


# In[12]:


### Binary Files

# Writing to a binary file
data = b'\x00\x01\x02\x03\x04'
with open('example.bin', 'wb') as file:
    file.write(data)


# In[13]:


# Reading a binary file
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)


# In[14]:


### Read the content froma  source text fiile and write to a destination text file
# Copying a text file
with open('example.txt', 'r') as source_file:
    content = source_file.read()

with open('destination.txt', 'w') as destination_file:
    destination_file.write(content)


# In[ ]:


#Read a text file and count the number of lines, words, and characters.
# Counting lines, words, and characters in a text file
def count_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
    return line_count, word_count, char_count

file_path = 'example.txt'
lines, words, characters = count_text_file(file_path)
print(f'Lines: {lines}, Words: {words}, Characters: {characters}')


# The w+ mode in Python is used to open a file for both reading and writing. If the file does not exist, it will be created. If the file exists, its content is truncated (i.e., the file is overwritten).

# In[17]:


### Writing and then reading a file

with open('example.txt','w+') as file:
    file.write("Hello world\n")
    file.write("This is a new line \n")

    ## Move the file cursor to the beginning
    file.seek(0)

    ## Read the content of the file
    content=file.read()
    print(content)


# In[ ]:





# In[ ]:





# In[ ]:




