#!/usr/bin/env python
# coding: utf-8

# ##CONDITINAL STATEMENT
# if , elif , else

# In[2]:


n1=int(input("Enter a number:"))
if n1%2==0:
    print("number {} is even".format(n1))
else:
    print("number {} is odd".format(n1))


# In[3]:


n1=int(input("Enter a number:"))
if n1%2==0:
    print("number {} is even".format(n1))
else:
    print("number {} is odd".format(n1))


# ##comparision operator 
# .==equal to
# .< less than 
# .> greater than

# In[5]:


l1=["python","c++","c"]
print(l1)
i=input("select your program:")
if i in l1:
    print("True: These are programing languages ",i)
else:
    print("This is not belongs to above skill")


# In[9]:


l1=["python","c++","c"]
print(l1)
i=input("select your program:")
if i =="c":
    print("True: These are programing languages belongs to ",i)
elif i=="python":
    print("this is{} language".format(i))
else:
    print("This is not belongs to above skill")


# ### Write a program that takes the age of the dog as an input and calculates the equivalent age in human years

# In[11]:


dog_age=int(input("age of Dog"))
if dog_age<0:
    print("not possible")
elif dog_age==0:
    print("Its Zero human year")
elif dog_age==1:
    print("approx 14 human years")
else:
    human=dog_age+14
    print("its belongs to "+str(human)+"human years")


# #### 1. Write a program to read 3 float numbers and print the largest value

# In[14]:


n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
n3=int(input("Enter 3rd number:"))
if n1>n2:
    g1=n1
else:
    g1=n2
if n1>n3:
    g2=n1
else:
    g2=n3
if g1>g2:
    print(str(g1)+ "is greater")
else:
    print(str(g2)+ "is greater")


# # LOOPS
# ##for loop
# #while loop

# ## Store the monthly expenses in a list and find out the total expenses for all month

# In[5]:


exp=[15000,20000,18000,25000]
total=exp[0]+exp[1]+exp[2]+exp[3]
total


# In[8]:


t1=0
for i in exp:
    t1=t1+i
print(t1)


# In[13]:


exp=[15000,20000,18000,25000]
t1=0


# In[18]:


for i in range(len(exp)):
    print(i)
    print("month ",(i+1),"expenses",exp[i])
    print(exp[i])
    t1=t1+exp[i]
print("total expenses",t1)


# In[16]:


for p in range(1 ,16):
    print(p)


# ##for loop with break statement

# In[20]:


key="chair"
l1=["table","room1","kitchen","chair","hall"]
for i in l1:
    if i==key:
        print("we got key")
        break
    else:
        print("we haven't found key")


# ### for loop with continue statement
# 

# In[22]:


for i in range(1,15):
    if i%2==0:
        continue
    print(i)


# In[24]:


for i in range(1,10):
    if i>=5:
        continue
    print(i)


# #while loop
# #take only one statement
# #its have increment /decrement with have acounter

# In[4]:


#print 1to5
i=10
while i>=5:
    print(i)
    i=i-1


# In[5]:


###function


# In[2]:


num=int(input("enter you number"))
if num%2==0:
    print("number {} is even".format(num))
else:
    print("number {} is odd".format(num))
          


# In[3]:


def eve_odd(num):
    if num%2==0:
        print("number {} is even".format(num))
    else:
        print("number {} is odd".format(num)) 


# In[4]:


eve_odd(12)


# In[5]:


eve_odd(15)


# In[ ]:




