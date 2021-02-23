# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:16:36 2021

@author: nkfreeman
"""

def plot_histogram(data_samples, 
                   *,
                   fig_aspect = (6, 4),
                   num_bins = 'auto'):
    '''
    Plots histogram for provided  data_samples

    Parameters
    ----------
    data_samples : list, numpy array, or pandas Series
        Object containing data samples for histogram.
    fig_aspect : (int, int), optional
        Tuple specifying aspect ratio for figure. The default is (6, 4).
    num_bins : int, optional
        Number of bins to use for histogram. The default is 'auto'.

    Returns
    -------
    None.

    '''
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set_style('whitegrid')
    
    fig, ax = plt.subplots(1, 1, figsize = fig_aspect)
    
    ax.hist(
        data_samples,
        bins = num_bins,
        edgecolor = 'k',
    )
    
    plt.show()
    
    
def compare_histograms(data_sample1,
                       data_sample2,
                       *,
                       fig_aspect = (6, 4),
                       num_bins = 'auto'):
    '''
    Plots histogram for provided  data_samples

    Parameters
    ----------
    data_sample1 : list, numpy array, or pandas Series
        Object containing data samples for 1st histogram.
    data_sample2 : list, numpy array, or pandas Series
        Object containing data samples for 2nd histogram.
    fig_aspect : (int, int), optional
        Tuple specifying aspect ratio for figure. The default is (6, 4).
    num_bins : int, optional
        Number of bins to use for histogram. The default is 'auto'.

    Returns
    -------
    None.

    '''
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set_style('whitegrid')
    
    fig, ax = plt.subplots(1, 1, figsize = fig_aspect)
    
    ax.hist(
        data_sample1,
        bins = num_bins,
        alpha = 0.8,
        label = 'Sample 1',
        edgecolor = 'k',
    )
    
    ax.hist(
        data_sample2,
        bins = num_bins,
        alpha = 0.5,
        label = 'Sample 2',
        edgecolor = 'k',
    )
    
    ax.legend()
    
    plt.show()