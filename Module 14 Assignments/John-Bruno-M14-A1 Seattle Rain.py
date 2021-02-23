#!/usr/bin/env python
# coding: utf-8

# # M14-A1 Seattle Rain
# 
# # Instructions:
# You will be utilizing Seattle2014.csv for this assignment.
# 
# Create a function named **seattle_rain()**. From the .csv file, read in the precipitation values (denoted 'PRCP'). You will need to convert from centimeters to inches. Shape the data. Using Pandas + NumPy, you want to get the following values below:
# 
# ### Expected sample output:
# umber days without rain: 215<br>
# Number days with rain: 150<br>
# Days with more than 0.5 inches: 37<br>
# Rainy days with < 0.2 inches: 75<br>

# In[3]:


#Write your Python code here
import pandas as pd
import numpy as np

def seattle_rain():
    """ This function takes the file Seattle2014.csv, converts millimeters to inches, and outputs days 
    without rain, with rain, days with more than 0.5 inches and rainy days with less than 0.2 inches"""
    try:
        rain = pd.read_csv('Seattle2014.csv')['PRCP'].values
        inches = rain / 254.0  
        inches.shape

        print("SEATLE RAIN...\n\n")
        print("Number days without rain:", np.sum(inches == 0))
        print("Number days with rain:", np.sum(inches != 0))
        print("Days with more than 0.5 inches:", np.sum(inches > 0.5))
        print("Rainy days with < 0.2 inches:", np.sum((inches > 0) & (inches < 0.2)))

    
    except FileNotFoundError as e:
        print(e,"Please input correct file (Seattle2014.csv).")
    except NameError as e:
        print(e)
    except Exception as e:
        print(e)
        
seattle_rain()

