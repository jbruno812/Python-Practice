#!/usr/bin/env python
# coding: utf-8

# # Module 9, Assignment 1 - Error Handling
# 
# ## Objectives
# * Understand why and when to use error handling in Python
# * Be able to explain and use ```try...except``` blocks
# * Describe the purpose of an ```else``` statement within a ```try...except``` block
# * Describe the purpose of a ```finally``` statement within a ```try...except``` block
# * Demonstrate the ability to trap specific and general errors

# In[ ]:


# Write a function that accepts two parameters (an int for number of lines and the text file) that can be used 
#   to open a text file and display the first N lines of text. Provide appropriate error handling. 
#   Your error handling should provide exception handling for at least two specific errors.
#   Name the function read_lines_of_text()


# In[1]:


def read_lines_of_text(N, file):
    """This function takes a number to indicate number of lines and
    a text file as parameters to output the lines in the file"""
    try:
        with open(file, "r") as f:   
            lines_in_files = len(f.readlines())
            if(lines_in_files < N):
                    raise StopIteration("The number input is higher than amount of lines in file.")
        with open(file, "r") as file2:  
            for i in range(N):
                print(file2.readline())

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

read_lines_of_text(3,'untitled.txt')

