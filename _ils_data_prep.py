# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:11:37 2021

@author: nkfreeman
"""

def get_ils_data(data_path):
    '''
    This function reads the Iowa Liquor Sales sample we are using and 
    performs some basic type conversions.

    Parameters
    ----------
    data_path : pathlib Path object
        pathlib Path object describing location of raw data file, which should
        be a CSV file compressed using GZIP compression.

    Returns
    -------
    data : pandas DataFrame
        pandas DataFrame containing the converted data.

    '''
    
    import pandas as pd
    data = pd.read_csv(data_path, compression = 'gzip')
    
    int_columns = [
        'Store Number',
        'County Number',
    ]
    
    for col in int_columns:
        data[col] = data[col].astype(int)
        
    data['Week Start'] = pd.to_datetime(data['Week Start'])
    
    return data