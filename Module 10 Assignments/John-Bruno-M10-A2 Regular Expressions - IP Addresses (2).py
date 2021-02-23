#!/usr/bin/env python
# coding: utf-8

# # M10-A2 Regular Expressions - IP Addresses
# 
# # Instructions:
# You will be utilizing mbox.txt for this assignment. To work with a local copy of mbox-short.txt, download it from the course Github repository. 
# 
# In this excercise, you will use regular expressions to find all IP addresses contained in the mbox-short.txt file. You will return two numbers each on their own line. The first number represents the total number of IP addresses found in the mbox-short.txt file. The second is the number of unique IP addresses contained in mbox-short.txt. Finally, print a sorted list of all unique IP addresses. Do all of this in a function named **get_ip_addresses** that returns the sorted list of unique IP addresses. Print the sorted list.
# 
# As always, your program should be reasonably efficient, utilize docstrings, dynamic pathing, and utilize error handling.
# 
# ### Expected sample output:
# All IP addresses: 189<br>
# Unique IP addresses: 31<br>
# ['127.0.0.1', '134.68.220.122', '141.211.14.25', '141.211.14.34', '141.211.14.36', '141.211.14.39', '141.211.14.43', '141.211.14.46', '141.211.14.58', '141.211.14.72', '141.211.14.76', '141.211.14.79', '141.211.14.83', '141.211.14.84', '141.211.14.90', '141.211.14.91', '141.211.14.92', '141.211.14.93', '141.211.14.97', '141.211.14.98', '141.211.93.141', '141.211.93.142', '141.211.93.143', '141.211.93.144', '141.211.93.145', '141.211.93.149', '141.211.93.151', '141.211.93.152', '141.211.93.153', '194.35.219.182', '194.35.219.184']

# In[36]:


#Write your Python code here
import re
def get_ip_addresses(file):
    """This function takes a file as parameter to output the total and unique count of IP addresses in the file
       and then sorting and listing those unique IP addresses."""
    try:
        with open(file, "r") as f:
            all_ip_list = []
            for line in f:
                line = line.rstrip()
                x = re.findall('\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                if len(x) > 0:
                    all_ip_list.extend(x)

        print('All IP addresses:' + " " + str(len(all_ip_list)))
        all_revs_set = set(all_ip_list)
        print('Unique IP addresses:' + " " + str(len(all_revs_set)))
        print (sorted(all_revs_set))
   
    except FileNotFoundError as e:
        print(e,"Please input correct file name.")
    except NameError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print("No Exceptions thrown.")
    finally:
        print("Opening file process completed.")
    

get_ip_addresses('mbox-short.txt')


# In[ ]:





# In[ ]:




