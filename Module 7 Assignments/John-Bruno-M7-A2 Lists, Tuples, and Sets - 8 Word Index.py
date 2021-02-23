#!/usr/bin/env python
# coding: utf-8

# # M7-A1 Lists, Dictionaries, and Tuples - 8 Word Index
# 
# # Instructions:
# Ask the user for 8 words and an index and output the word at the index using arrays
# 
# **Bold** indicates input from the console.
# 
# ### Expected sample output:
# Enter word 1<br>
# **Rat**<br>
# Enter word 2<br>
# **Cat**<br>
# Enter word 3<br>
# **Dog**<br>
# Enter word 4<br>
# **Mouse**<br>
# Enter word 5<br>
# **Cow**<br>
# Enter word 6<br>
# **Pig**<br>
# Enter word 7<br>
# **Chicken**<br>
# Enter word 8<br>
# **Elephant**<br>
# Enter index<br>
# **4**<br>
# The word at index 4 is Mouse<br>
# 
# ### Expected sample output:
# Enter word 1<br>
# **Rat**<br>
# Enter word 2<br>
# **Cat**<br>
# Enter word 3<br>
# **Dog**<br>
# Enter word 4<br>
# **Mouse**<br>
# Enter word 5<br>
# **Cow**<br>
# Enter word 6<br>
# **Pig**<br>
# Enter word 7<br>
# **Chicken**<br>
# Enter word 8<br>
# **Elephant**<br>
# Enter index<br>
# **5**<br>
# The word at index 5 is Cow<br>

# In[5]:


#Write your Python code here
a = input ('Enter word 1')
b = input ('Enter word 2')
c = input ('Enter word 3')
d = input ('Enter word 4')
e = input ('Enter word 5')
f = input ('Enter word 6')
g = input ('Enter word 7')
h = input ('Enter word 8')
i = input ('Enter index') 

i = int(i)
my_list = (a,b,c,d,e,f,g,h)
name = my_list[i-1]

print("The word at index" + " " + str(i) + " " + "is" " " + name)


# In[ ]:




