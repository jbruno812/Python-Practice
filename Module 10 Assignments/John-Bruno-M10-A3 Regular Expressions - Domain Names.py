#!/usr/bin/env python
# coding: utf-8

# # M10-A3 Regular Expressions - Domain Names
# 
# # Instructions:
# In this exercise, you'll use regular expressions to find four-level and five-level domain names in the EDU top-level domain within a semi-structured data file (mbox-short.txt). For example, server1.mail.cba.ua.edu (five-level hostname) db1.criminaljustice.ua.edu (four-level hostname) Using Python 3, create a script that finds all instances of four-level or five-level hostnames and that end in .edu. Report the number of hosts found (including duplicates). Then print the number of unique hostnames. Finally, present a sorted list of all the unique hostnames. This should be done in a function named **get_domain_names** that returns the sorted list. Then, print the sorted list.
# 
# As always, your program should be reasonably efficient, utilize docstrings, dynamic pathing, and utilize error handling. 
# 
# ### Expected Sample Output:
# All hosts: 216<br>
# Unique hosts: 29<br>
# [' anniehall.mr.itd.umich.edu ', ' carrie.mr.itd.umich.edu ', ' casino.mail.umich.edu ', ' chaos.mail.umich.edu ', ' creepshow.mr.itd.umich.edu ', ' dreamcatcher.mr.itd.umich.edu ', ' eyewitness.mr.itd.umich.edu ', ' faithful.mail.umich.edu ', ' fan.mail.umich.edu ', ' firestarter.mr.itd.umich.edu ', ' flawless.mail.umich.edu ', ' frankenstein.mail.umich.edu ', ' galaxyquest.mr.itd.umich.edu ', ' ghostbusters.mr.itd.umich.edu ', ' godsend.mail.umich.edu ', ' guys.mr.itd.umich.edu ', ' holes.mr.itd.umich.edu ', ' icestorm.mr.itd.umich.edu ', ' it.mr.itd.umich.edu ', ' jacknife.mail.umich.edu ', ' mission.mail.umich.edu ', ' nakamura.uits.iupui.edu ', ' panther.mail.umich.edu ', ' salemslot.mr.itd.umich.edu ', ' score.mail.umich.edu ', ' shining.mr.itd.umich.edu ', ' sleepers.mail.umich.edu ', ' tadpole.mr.itd.umich.edu ', ' workinggirl.mr.itd.umich.edu '] 29

# In[7]:


#write your Python code here
import re
def get_domain_names(file):
    """This function takes a file as parameter to output the total and unique count of 4 & 5-level hostnames 
    in the file and then listing those unique hostnames."""
    try:
        with open(file, "r") as f:
            all_emails_list = []
            for line in f:
                line = line.rstrip()
                x = re.findall('\w*\.*\w+\.\w+\.\w+\.edu', line)
                if len(x) > 0:
                    all_emails_list.extend(x)
#regexr.com/589g4
        print('All Hosts:' + " " + str(len(all_emails_list)))
        all_revs_set = set(all_emails_list)
        print('Unique Hosts:' + " " + str(len(all_revs_set)))
        print(sorted(all_revs_set), (str(len(all_revs_set))))
   
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
    

get_domain_names('mbox-short.txt')

