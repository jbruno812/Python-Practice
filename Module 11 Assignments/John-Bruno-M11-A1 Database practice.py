#!/usr/bin/env python
# coding: utf-8

# # Module 11, Assignment 1 
# Database Practice
# 
# Learning objectives in this module:
# * Use the standard library to create a SQLite database
# * Design a simple database to hold contact information (name, address, email, phone)
# * Select appropriate SQLite data types
# * Implement a database connection and cursor in Python
# * Execute SQL commands on a SQLite database using Python
# * Become familiar with SQLite Studio
# * Apply error handling to a database Python application

# In[ ]:


# Using Python create a database called "<name>_contacts", e.g., "greg_contacts.sqlite", then connect
import sqlite3

conn = sqlite3.connect('john_contacts.sqlite') 
cur = conn.cursor()


# In[ ]:


# Add a People table to your database and then Add first_name and last_name fields to the table. Use appropriate datatypes.
cur.execute("""CREATE TABLE People(
                                    first_name TEXT,                                    
                                    last_name TEXT)""") 
conn.close()


# In[ ]:


# Using SQLiteStudio (or your preferred application), add additional fields (at least person_id [primary key, auto-incrementing], 
#   address, city, state, zip, and email), and then create a DDL file for the database described above and store it 
#   in a variable called my_table.

my_table = """ CREATE TABLE People (
    person_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name  TEXT,
    address    VARCHAR,
    city       TEXT,
    state      TEXT,
    zip        CHAR,
    email      VARCHAR); """


# In[ ]:


# Delete the People table
cur.execute('DROP TABLE IF EXISTS People')
conn.close()


# In[ ]:


# Using the DDL file, re-create the people table. If the DDL contains more than one statment (e.g., more than 1 semi-colon), 
#   use executescript() instead of execute()
cur.execute(""" CREATE TABLE People (
    person_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name  TEXT,
    address    VARCHAR,
    city       TEXT,
    state      TEXT,
    zip        CHAR,
    email      VARCHAR); """)
conn.commit()
conn.close()


# In[31]:


# Create a function called list_records function that displays all records in the people database
def list_records():
    cur.execute('SELECT * FROM People')
    print("All People:")
    for row in cur:
        print(row)


# In[34]:


# Add a single person to yout contact database (you only need to use first name, last name, and email)
cur.execute('INSERT INTO People (first_name, last_name, email) values (?,?,?)', ('John.', 'Bruno', 'ljbruno@crimson.ua.edu'))
conn.commit()
conn.close()


# In[36]:


# Call the list_records function
list_records()


# In[41]:


# Simultaneously add 3 people to your contact database
People = [('Nathaniel','B'),
          ('Melinda','B'),
          ('Hannah', 'B')]
cur.executemany('INSERT INTO People (first_name, last_name) values (?,?)', People)
conn.commit()
conn.close()


# In[42]:


# Call the list records function again
list_records()

