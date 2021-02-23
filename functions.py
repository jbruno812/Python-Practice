# -*- coding: utf-8 -*-

import requests
import time


def io_bound_task(index_value, global_start_time):
    
    start_time = time.time()
    start_time = round(start_time - global_start_time, 2)
    print(f'Task {index_value} started at time {start_time}')

    url = 'https://httpbin.org/drip'
    params = {
        'numbytes': index_value,
    }
    r = requests.get(url, params = params)
    
    end_time = time.time()
    end_time = round(end_time - global_start_time, 2)
    print(f'Task {index_value} ended at time {end_time}')

    return r.text


def cpu_bound_task(index_value, global_start_time, count):
    
    import random
    
    start_time = time.time()
    start_time = round(start_time - global_start_time, 2)
    print(f'Task {index_value} started at time {start_time}')

    mylist = []
    for i in range(count):
        mylist.append(random.random())
    
    end_time = time.time()
    end_time = round(end_time - global_start_time, 2)
    print(f'Task {index_value} ended at time {end_time}')

    return sum(mylist)
