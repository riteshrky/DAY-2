#!/usr/bin/env python
# coding: utf-8

# In[1]:


def say_hello(name):
    print("hello",name)
    print ("how are you ")


# In[2]:


say_hello("Jam")


# In[3]:


# write a function to print sum of three numbers
def sum_of_num(x,y,z=10):#x,y are positional argumnets, and z is kerywords
    print(x+y+z)


# In[4]:


sum_of_num(50,60)


# In[5]:


sum_of_num(50,60,40)#keywors assign value


# In[6]:


marks1=[50,70,88,95,75]
marks2=[40,90,60,55,80]

total=0
for i in marks1:
    total=total+i
print(total)

total=0
for i in marks2:
    total=total+i
print(total)


# In[10]:


def marks_sum(marks):
    t1=0
    for i in marks:
        t1=t1+i
    return(t1)

s=marks_sum(marks1)
print(s)
    


# In[11]:


s1=marks_sum(marks2)
print(s1)


# In[14]:


#Absoulte value
def abs_value(num):
    if num<0:
        return(-num)
    else:
        return(num)
    
a1=abs_value(-9)
print(a1)


# In[15]:


a2=abs_value(8)
print(a2)


# In[16]:


def name(n1,age=32):
    print("hello i am {} and my age is {}".format(n1,age))
    
name("Rathi")


# In[17]:


name("Rathi",28)


# In[2]:


## Given a list, write a fn to calculate the sum of all even numbers and all odds numbers
lst1=[70,33,80,61,88,85,76,63,74,72]
def ev_od(lst):
    ev_sum=0
    od_sum=0
    for i in lst:
        if i%2==0:
            ev_sum=ev_sum+i
        else:
            od_sum=od_sum+i
    return(ev_sum,od_sum)

ev_od(lst1)
          


# In[7]:


lst1=[70,33,80,61,88,85,76,63,74,72]# 
def eve_odd(lst):
    if lst%2==0:# this thing not contain lists, ints
        return  "Even"
    else:
        return "odd"

s=eve_odd(55)
print(s)


# In[8]:


map(eve_odd,lst1)


# In[9]:


list(map(eve_odd,lst1))


# In[10]:


##Lamnda /anonymous function

def add(a,b):
    s1=a+b
    return s1

s=add(2,3)
print(s)


# In[15]:


s2=lambda a,b:a+b #lambda input and operation
s2(30,60)


# In[16]:


l1=[45,67,85]
l2=[34,56,98]
ad1=list(map(lambda x,y:x+y, l1,l2))


# In[17]:


print(ad1)


# In[18]:


ad2=map(lambda x,y:x+y,l1,l2)
print(ad2)


# In[19]:


print(list(ad2))


# In[20]:


## create 2 function to add (add_num())and multiply 2 numbers
#for addition
sum=lambda a,b:a+b
sum(45,36)


# In[23]:


#for multiplication
mul=lambda c,d:c*d
mul(4,5)


# In[8]:


##average of marks
###write a function to cal the average marks.
###write a function to cal the grade of the students based on avg marks (if,elif,else)
marks1=[70,50,97,66,99]

def avg_marks(marks):
    
    
    s1=0
    for i in marks:
        s1=s1+i
        avg=s1/len(marks)
        
        if avg>=90:
            Grade="Grade A"
        elif avg>=80 and avg<=90:
            Grade="Grade B"
        elif avg>=70 and avg<=80:
            Grade="Grade C"
        else:
            Grade="Grade D"
    return (avg,Grade)

s1=avg_marks(marks1)
print(s1)

    


# In[12]:


ls=[]
for i in range(50):
    if i%2==0:
        ls.append(i)
print(ls)


# In[15]:


ls=[i for i in range(50) if i%3==0]
print(ls)


# In[ ]:




