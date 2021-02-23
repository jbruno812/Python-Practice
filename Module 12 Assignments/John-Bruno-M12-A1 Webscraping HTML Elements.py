#!/usr/bin/env python
# coding: utf-8

# # Basic Web Scraping Using Beautiful Soup
# 
# This is a multi-part webscraping Python assignment. Please follow each segment of directions.
# 
# As always, your code should be reasonably efficient, utilize docstrings where necessary, and use appropriate error-handling.

# In[146]:


import requests
from bs4 import BeautifulSoup as soup
import bs4
import pandas as pd


# ## Web site to scrape
# Below is the URL from which you will scrape the name, title and phone number for each faculty member at Lamar School.

# In[6]:


url = "http://www.lamarschool.com/about-us/faculty.cfm"


# ## Initialize headers and get the HTML page

# In[8]:


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

r = requests.get(url, headers=headers)

print(str(r.content)[:1000])


# ## Parse the HTML

# In[14]:


# Use Beautiful Soup to parse the HTML. 
# Pass the HTML page (.content returns bytes, .text returns string) and use the "html.parser"
soup = bs4.BeautifulSoup(r.content, 'html.parser')

# Optional: print the soup object you created above


# In[15]:


# Print the title of the web site to verify you have successfully parsed the page
soup.title 


# ## Scrape name, title and phone number
# Now that you have successfully retrieved the HTML for the faculty page, next we want to scrape the faculty name, title, and number.
# 
# Once you have scraped the data return and print a formatted list of the facutly names, titles phone numbers similar the example below:
# 
# ```
# Adams, Shane
#   Title:  Dir of Athletics and  Facilities
#   Phone:  601-482-1345 
# 
# Alexander, Danny
#   Title:  HS Science
#   Phone:  601-482-1345 
# 
# Autry, Bill
#   Title:  Tennis Coach
#   Phone:  601-482-1345 
# ```
# 
# Do this in an assignment named **info_scraping()** that returns the formatted list. Remember to print the formatted list as well.

# In[212]:


# Scrape faculty name, title, and phone number

def info_scraping():
    """ This function takes the name, title, and phones of the faculty at the url:http://www.lamarschool.com/about-us/faculty.cfm
         then formats and displays them""" 
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content)
    faculty_data = soup.find_all('tr',{'class':'directory-row dir-row dir-border'})

    for i,f in enumerate(faculty_data,1):
        try:
            names = f.find('td', attrs = {'class':'dir-name'}).text.strip()
            titles = f.find('td', attrs = {'class':'dir-col2'}).text.strip()
            phones = f.find('td', attrs = {'class':'dir-col4'}).text.strip()
            faculty_final = "{}\n " " " " Title: " " " " {}\n " " " " Contact: {} \n".format(names, titles, phones)
            print(faculty_final)
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)


# In[213]:


# Print formatted listing of faculty name, title, phone
info_scraping()


# In[ ]:




