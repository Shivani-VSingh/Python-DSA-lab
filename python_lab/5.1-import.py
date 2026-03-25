#!/usr/bin/env python
# coding: utf-8

# ##### Importing Modules in Python: Modules and Packages
# In Python, modules and packages help organize and reuse code. Here's a comprehensive guide on how to import them.

# In[1]:


import math
math.sqrt(16)


# In[2]:


from math import sqrt,pi
print(sqrt(16))
print(sqrt(25))
print(pi)


# In[5]:


import numpy as np
np.array([1,2,3,4])


# In[7]:


from math import *
print(sqrt(16))
print(pi)


# In[14]:


from package.maths import addition
addition(2,3)


# In[23]:


from package import maths
maths.addition(2,3)


# #### Conclusion
# Importing modules and packages in Python allows you to organize your code, reuse functionalities, and keep your projects clean and manageable. By understanding how to import modules, specific functions, and use relative imports within packages, you can structure your Python applications more effectively.

# 
