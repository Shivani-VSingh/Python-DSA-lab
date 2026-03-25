#!/usr/bin/env python
# coding: utf-8

# #### Loops
# Video Outline:
# 1. Introduction to Loops
# 2. for Loop
#    - Iterating over a range
#    - Iterating over a string
# 
# 3. while Loop
# 4. Loop Control Statements
#     - break
#     - continue
#     - pass
# 5. Nested Loops
# 6. Practical Examples and Common Errors

# In[1]:


range(5)


# In[2]:


## for loop

for i in range(5):
    print(i)


# In[3]:


for i in range(1,6):
    print(i)


# In[7]:


for i in range(1,10,2):
    print(i)


# In[8]:


for i in range(10,1,-1):
    print(i)


# In[9]:


for i in range(10,1,-2):
    print(i)


# In[10]:


## strings

str="Krish Naik"

for i in str:
    print(i)


# In[11]:


## while loop

## The while loop continues to execute as long as the condition is True.

count=0

while count<5:
    print(count)
    count=count+1




# In[14]:


## Loop Control Statements

## break
## The break statement exits the loop permaturely

## break sstatement

for i in range(10):
    if i==5:
        break
    print(i)
   


# In[15]:


## continue

## The continue statement skips the current iteration and continues with the next.

for i in range(10):
    if i%2==0:
        continue
    print(i)




# In[18]:


## pass
## The pass statement is a null operation; it does nothing.

for i in range(5):
    if i==3:
        pass
    print(i)


# In[19]:


## Nested loopss
## a loop inside a loop

for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")


# In[20]:


## Examples- Calculate the sum of first N natural numbers using a while and for loop

## while loop  

n=10   
sum=0
count=1

while count<=n:
    sum=sum+count
    count=count+1

print("Sum of first 10 natural number:",sum)


# In[21]:


n=10   
sum=0
for i in range(11):
    sum=sum+i

print(sum)


# In[22]:


## Example- Prime numbers between 1 and 100

for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


# #### Conclusion:
# Loops are powerful constructs in Python that allow you to execute a block of code multiple times. By understanding and using for and while loops, along with loop control statements like break, continue, and pass, you can handle a wide range of programming tasks efficiently.

# In[ ]:




