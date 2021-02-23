#!/usr/bin/env python
# coding: utf-8

# # Module 13, Assignment 1 - Numpy Basics
# Please print the arrays as described below.
# 

# In[4]:


import numpy as np
# After importing NumPy as np, create a one-dimensional array of random integers

# Made below comment to check for error handling.

###  random_array = np.random.randint(2, 10, size=6)


# Create one function called m13_a1 that executes all the parts of this assignment.
def m13_a1():
    """This function creates and outputs all of the parts of assignment M13 NumPy Basics."""
    try:

        # Brought this task from above into function.
        random_array = np.random.randint(2, 10, size=6)

        # Manually create and print a two-dimensional array of floats.
        array_1 = np.array([[1.0,2.0,3.0,4.0],
                            [5.0,6.0,7.0,8.0]])


        # Create a two dimensional array (6x6) of 0's.
        array_0s = np.zeros((6,6))

        # Create a two-dimensional array of (5x7) of 1's.
        array_1s = np.ones((5,7))


        # Create an array with 50 evenly spaced values between 10 and 100.
        my_array = np.linspace(10, 100, 50)


        # Create 2 4 x 4 arrays with random integers (1-100) and then add them.

        array_3 = np.random.randint(1,100, size=(4,4))
        array_4 = np.random.randint(1,100, size=(4,4))

        array_add = (array_3 + array_4)
        
        # Return statement
        
        return random_array, array_1, array_0s, array_1s, my_array, array_add

    
    # Error handling for missing NumPy.
    
    except NameError as e:
        print(e, "Make sure that you are importing numpy as np.")
    else:
        print("No Exceptions thrown.")

m13_a1()


# In[ ]:




