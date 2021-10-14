#!/usr/bin/env python
# coding: utf-8

# In[1]:


def temp_con(x):
    
    
    if (x>0):
        y=(x-273)*9/5+32
    return(y)

print(temp_con(273))
print(temp_con(-12))


# In[ ]:


def temp_con(x):
    try:
        if (x>0):
            y=(x-273)*9/5+32
        return(y)
    except UnboundLocalError as ax:
        print("Enter greater value")

