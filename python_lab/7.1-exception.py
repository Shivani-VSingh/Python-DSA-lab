#!/usr/bin/env python
# coding: utf-8

# #### Understanding Exceptions
# 
# Exception handling in Python allows you to handle errors gracefully and take corrective actions without stopping the execution of the program. This lesson will cover the basics of exceptions, including how to use try, except, else, and finally blocks.

# ##### What Are Exceptions?
# Exceptions are events that disrupt the normal flow of a program. They occur when an error is encountered during program execution. Common exceptions include:
# 
# - ZeroDivisionError: Dividing by zero.
# - FileNotFoundError: File not found.
# - ValueError: Invalid value.
# - TypeError: Invalid type.

# In[3]:


## Exception try ,except block

try:
    a=b
except:
    print("The variable has not been assigned")


# In[4]:


a=b


# In[5]:


try:
    a=b
except NameError as ex:
    print(ex)


# In[8]:


try:
    result=1/0
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")


# In[11]:


try:
    result=1/2
    a=b
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")
except Exception as ex1:
    print(ex1)
    print('Main exception got caught here')


# In[14]:


try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than 0")
except Exception as ex:
    print(ex)


# In[16]:


## try,except,else block
try:
    num=int(input("Enter a number:"))
    result=10/num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}")

    



# In[18]:


## try,except,else and finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"The result is {result}")
finally:
    print("Execution complete.")



# In[25]:


### File handling and Exception HAndling

try:
    file=open('example1.txt','r')
    content=file.read()
    a=b
    print(content)

except FileNotFoundError:
    print("The file does not exists")
except Exception as ex:
    print(ex)

finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print('file close')


# In[22]:


if 'file' in locals():
    print(True)


# In[24]:


not file.closed()


# In[ ]:




