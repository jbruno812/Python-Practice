# -*- coding: utf-8 -*-
import concurrent.futures as cf
import time

import functions

if __name__ == '__main__':
    
    global_start_time = time.time()
    num_tasks = 10
    num_workers = 7
    numbers_to_generate = 10000000
    
    data = {}
    
    # for i in range(1, num_tasks + 1):
    #     response = functions.io_bound_task(i, global_start_time)
    #     data[i] = response
    
    # with cf.ThreadPoolExecutor(max_workers = num_workers) as executor:
    #     futures = {}
    #     for i in range(1, num_tasks + 1):
    #         futures[executor.submit(functions.io_bound_task,
    #                                 i, global_start_time)] = i
            
    #     for future in cf.as_completed(futures):
    #         index = futures[future]
    #         data[index] = future.result()
    
    
    
    # for i in range(1, num_tasks + 1):
    #     response = functions.cpu_bound_task(i, global_start_time, numbers_to_generate)
    #     data[i] = response
    
    
    # with cf.ThreadPoolExecutor(max_workers = num_workers) as executor:
    #     futures = {}
    #     for i in range(1, num_tasks + 1):
    #         futures[executor.submit(functions.cpu_bound_task,
    #                                 i, global_start_time, numbers_to_generate)] = i
            
    #     for future in cf.as_completed(futures):
    #         index = futures[future]
    #         data[index] = future.result()
            
    
    # start = time.time()
    # with cf.ProcessPoolExecutor() as executor:
    #     futures = {}
    #     for i in range(1, num_tasks + 1):
    #         futures[executor.submit(functions.cpu_bound_task,
    #                                 i, global_start_time, numbers_to_generate)] = i
            
    #     for future in cf.as_completed(futures):
    #         index = futures[future]
    #         data[index] = future.result()
    # end = time.time()
    # elapsed_time = round(end-start, 2)
    # print(elapsed_time)
