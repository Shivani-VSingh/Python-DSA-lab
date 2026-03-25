#!/usr/bin/env python
# coding: utf-8

# ### Syntax and Semantics in Python
# Video Outline:
# - Single line Comments and multiline comments 
# - Definition of Syntax and Semantics
# - Basic Syntax Rules in Python
# - Understanding Semantics in Python
# - Common Syntax Errors and How to Avoid Them
# - Practical Code Examples

# Syntax refers to the set of rules that defines the combinations of symbols that are considered to be correctly structured programs in a language. In simpler terms, syntax is about the correct arrangement of words and symbols in a code.
# 
# Semantics refers to the meaning or the interpretation of the symbols, characters, and commands in a language. It is about what the code is supposed to do when it runs.

# In[1]:


## Basic Syntax Rules In Python
## Case sensitivity- Python is case sensitive

name="Krish"
Name="Naik"

print(name)
print(Name)


# ### Indentation
# Indentation in Python is used to define the structure and hierarchy of the code. Unlike many other programming languages that use braces {} to delimit blocks of code, Python uses indentation to determine the grouping of statements. This means that all the statements within a block must be indented at the same level.

# In[2]:


## Indentation
## Python uses indentation to define blocks of code. Consistent use of spaces (commonly 4) or a tab is required.

age=32
if age>30:
    
    print(age)
    
print(age)


# In[3]:


## This is a single line comment
print("Hello World")


# In[5]:


## Line Continuation
##Use a backslash (\) to continue a statement to the next line

total=1+2+3+4+5+6+7+\
4+5+6

print(total)


# In[6]:


## Multiple Statements on a single line
x=5;y=10;z=x+y
print(z)


# In[7]:


##Understand  Semnatics In Python
# variable assignment
age=32 ##age is an integer
name="Krish" ##name is a string


# In[10]:


type(age)


# In[9]:


type(name)


# In[12]:


## Type Inference
variable=10
print(type(variable))
variable="Krish"
print(type(variable))


# In[14]:


age=32
if age>30:
    print(age)


# In[15]:


## Name Error
a=b


# In[17]:


## Code exmaples of indentation
if True:
    print("Correct Indentation")
    if False:
        print("This ont print")
    print("This will print")
print("Outside the if block")


# ### Conclusion:
# Understanding the syntax and semantics of Python is crucial for writing correct and meaningful programs. Syntax ensures the code is properly structured, while semantics ensures the code behaves as expected. Mastering these concepts will help in writing efficient and error-free Python code.

# 
