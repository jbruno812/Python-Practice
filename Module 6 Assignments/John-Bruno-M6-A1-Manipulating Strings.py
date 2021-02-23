#!/usr/bin/env python
# coding: utf-8

# # M6-A1 Manipulating Strings

# In[ ]:


# Create a function that receives named parameters for an address (first name, last name, street, city, state, zip) and
#   returns a formatted address:
#   Greg Bott
#   361 Stadium Dr.
#   Tuscaloosa, AL 35487
#
#   Name the function format_address()

#### THIS IS FUNCTION ATTEMPT, COULDN'T FIGURE OUT IT USING FUNCTION
def format_address(a,b,c,d,e,f):
    
    

    a = input ('Type first name')
    b = input ('Type last name')
    c = input ('Type street name')
    d = input ('Type city')
    e = input ('Type state')
    f = input ('Type zip')

    return (a + " " + b + "\n" + c + "\n" + d+"," + " " + e + " " + f)
format_address(a,b,c,d,e,f)

#### This is correct format but no function

a = input ('Type first name')
b = input ('Type last name')
c = input ('Type street name')
d = input ('Type city')
e = input ('Type state')
f = input ('Type zip')

print(a + " " + b + "\n" + c + "\n" + d+"," + " " + e + " " + f)


# In[ ]:


# Create a function that accepts one or more words, finds the longest word and returns that word and its character length
#   Name the function find_longest_word()
def find_longest_word(word_list):  
    longest_word =  max(word_list, key=len)
    return longest_word


# In[24]:


# Create a function that can accept first name - last name in one of two formats (first last or last, first) and return the opposite.
#    Name the function name_swap()
#    For example name_swap("Bott, Greg") would return "Greg Bott" and vice versa

def name_swap(x,y):
    print (y + "," + " " + x) 
    print(x +" "+ y)
    return name_swap
x = input("Type first name:")
y = input("Type last name:")
name_swap(x,y)


# In[ ]:


# Create a function that accepts a single word and returns the reverse of that word.
#   Name the function reverse_word.
def reverse_word(x):
  return x[::-1]
## found that ::-1 will do exactly what I needed to do

