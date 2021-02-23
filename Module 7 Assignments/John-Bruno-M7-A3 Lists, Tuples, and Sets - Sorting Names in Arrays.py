#!/usr/bin/env python
# coding: utf-8

# # M7-A1 Lists, Tuples, and Sets - Sorting Names in Arrays
# 
# # Instructions:
# Ask the user for the number of names in a list and get the names from the user. Sort the names and output them in the array format, aka: print(array)
# 
# **Bold** indicates input from the console.
# 
# ### Expected sample output:
# How many names are in your list?<br>
# **5**<br>
# Enter name<br>
# **Jerry**<br>
# Enter name<br>
# **Jacob**<br>
# Enter name<br>
# **Justin**<br>
# Enter name<br>
# **Jared**<br>
# Enter name<br>
# **Jobe**<br>
# ['Jacob', 'Jared', 'Jerry', 'Jobe', 'Justin']<br>
# 
# ### Expected sample output:
# How many names are in your list?<br>
# **9**<br>
# Enter name<br>
# **Sam**<br>
# Enter name<br>
# **Lauren**<br>
# Enter name<br>
# **Karen**<br>
# Enter name<br>
# **Jared**<br>
# Enter name<br>
# **Liz**<br>
# Enter name<br>
# **Zachary**<br>
# Enter name<br>
# **Allison**<br>
# Enter name<br>
# **Marylin**<br>
# Enter name<br>
# **Cary**<br>
# ['Allison', 'Cary', 'Jared', 'Karen', 'Lauren', 'Liz', 'Marylin', 'Sam', 'Zachary']<br>

# In[ ]:


#Write your Python code here
list =[]
number = int(input("how many names are in your list: "))
for i in range(0,number):    
    names = (input("Enter name:"))
    list.append(names)
print(list)

