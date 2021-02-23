#!/usr/bin/env python
# coding: utf-8

# # List Exercises

# In[41]:


# Create a function that can receive a list as its parameter and return the sum printed like this: 3 + 5 + 8 = 16
#   Name the function: expanded_sum()
def expanded_sum(*x):
    """function that takes three numbers as a list to print the addition and sum"""
    return print(x[0], "+", x[1], "+", x[2], "=", sum(x)) 

expanded_sum(3,5,8)
    
             


# In[43]:


# Create a function that takes a list as parameter and returns a list containing only the lowest and highest number (in that order)
#   Name the function: get_high_low()
def get_high_low(*x):
    return min(x), max(x) 

get_high_low(3,5,2,5)


# In[51]:


# Create a function that returns True if a list passed to it is empty.
#   Name the function: is_list_empty()
def is_list_empty(*x):
    if not x:
        print(True)
    return 
is_list_empty()


# In[58]:


# Create a function that takes two lists and returns True if they have at least one common member.
#   Name the function common_member()
def common_member(list1, list2):
    for x in list1:
        for y in list2:
            if x==y:
                check = True
                return check
common_member((1,3), (7,3,5))

