#!/usr/bin/env python
# coding: utf-8

# ###DAY 2
# ##String-
# string is immutable

# In[1]:


s="hello"


# In[2]:


s


# In[3]:


type(s)


# In[4]:


s[0]


# In[5]:


s[1]


# In[6]:


s[0]='k'


# In[7]:


s.upper()


# In[8]:


'This is me'.split()


# In[9]:


'my name is Rites'.split('y')


# In[10]:


'This is my class'.split()


# In[11]:


record='12012,Gurgaon,India'.split(',')


# In[14]:


pin=record[0]
city=record[1]
country=record[2]


# In[15]:


pin


# In[16]:


city


# In[17]:


country


# In[18]:


a='hello'
b='world'


# In[26]:


print(" ".join([a,b]))


# In[27]:


a+' '+b


# In[28]:


c=20


# In[29]:


print(a+str(c))


# ##Indexing

# In[30]:


text="ice cream"


# In[31]:


text[0]


# In[32]:


text[5]


# In[33]:


text[-3]


# In[34]:


text[1:3]


# In[35]:


text[:7]


# ##LIST
# list is mutable
# list is collection of data
# denaoted=[]

# In[36]:


n1=[3, 4,7,8,9]


# In[37]:


n1.append(12)


# In[38]:


n1


# In[39]:


n1.extend([90,32]) #here we enterd list to extend the list


# In[40]:


n1


# In[41]:


n1.insert(2,24)# insert in Indexing2is index and 24 is value


# In[42]:


n1


# In[43]:


n1.remove(7)# remove the data from list


# In[44]:


n1


# In[50]:


n1.pop()#its remove from last##### question with pop multiple times enter pop we see data remove multiples times


# In[51]:


n1


# In[52]:


n1.pop(1)


# In[53]:


n1


# In[56]:


del n1[3:]


# In[57]:


n1


# In[58]:


### inbuilt function


# In[59]:


n2=[12,14,18,24,36]


# In[60]:


min(n2)


# In[61]:


max(n2)


# In[62]:


sum(n2)


# In[63]:


name=["Jhon","karan","Daniel","Lynn"]
age=[34,45,28,44]


# In[64]:


na=[name,age]


# In[65]:


na


# In[66]:


na[1][3]


# ###SET
# UNODERED COLLECTION OF DATA TYPE
# NO DUBLICATE ELEMENTS
# DENOTED=SET{}

# In[67]:


a={1,3,7,4,9}


# In[68]:


type(a)


# In[69]:


a


# In[70]:


a[1]#its not support indexing


# In[71]:


m1={"hulk","iron","super"}


# In[72]:


m1.add("shadow")


# In[73]:


m1


# In[74]:


s1={"a","b","d","h","k"}
s2={"a","b","c","h","e"}


# In[76]:


s1.difference(s2)


# ##TUPLEs
# immutable
# indexing is done

# In[78]:


t1=("RAM","SHAM","DAM")


# In[79]:


t1[0]


# In[80]:


t1[1]


# In[82]:


t1[0]="jam"


# In[83]:


t1.index("RAM")


# Dictionaries
# .sequences in key - values pairs
# .Mutable
# .Iterable
# .dict={}

# In[84]:


d1={"car":4000000,"bike":80000,"cycle":5000}


# In[85]:


d1["auto"]=200000


# In[86]:


d1


# In[87]:


d2={"e-bike":90000,"bus":10000000}


# In[88]:


d1.update(d2)


# In[89]:


d1


# In[90]:


d1["car"]


# In[91]:


d1.keys


# In[92]:


d1.keys()


# In[93]:


d1.values()


# In[94]:


for x in d1.values():
    print(x)


# In[96]:





# In[ ]:




