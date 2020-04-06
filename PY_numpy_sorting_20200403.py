# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:14:47 2020

@author: Cipriandan

1. define list of sample size
2. for each element in the list_1: create random.normal()
3. for each element in the list_1
4.    for each element in the list_of_sorting_algorithms
5.        t0 = time.time()
6.        sort( sample_Iter_n, method = sort_iter )
7.        t1 = time.time()
8.        tt = t1 - t0
9.        add ( line to DataFrame )

......................... SORTING ................................
"""
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import time

start_pw = 4
stop_pw = 6
pw = np.arange( start_pw, stop_pw + 1,1 )
arr_ss = np.power( [ 10 ] * ( stop_pw - start_pw + 1) , pw )
arr_ss = np.hstack( (arr_ss,  np.multiply( [ 10**(stop_pw-1) ], range(2,91,1)) ) )
arr_ss = np.sort( arr_ss  )
 
arr_sk = np.array(['quicksort','mergesort','heapsort'])

col_names_1 = [ 'sample_size' ,'value']
df_nums = pd.DataFrame( columns = col_names_1 )
                       
col_names_2 = ['sort_type', 'sample_size', 'time_to_sort']
df_sort = pd.DataFrame( columns = col_names_2 )

big_sample_size = arr_ss[-1:]
the_values = np.random.normal( 0,1, big_sample_size ) * 1000

for iter_i in arr_ss:
    for iter_k in arr_sk:
        t0 = time.time()
        np_temp = np.sort( the_values[- iter_i:], 
                          kind = iter_k )
        t1 = time.time()
        tt = t1 - t0
        df_temp = pd.DataFrame({ 'sort_type':iter_k, 'sample_size':iter_i, 'time_to_sort':tt },index = [0])
        frames = [ df_sort, df_temp ]
        df_sort = pd.concat( frames )        
        del np_temp
        
sns.set_style("darkgrid")
g = sns.FacetGrid( df_sort,  hue = 'sort_type')
g = g.map(plt.scatter , 'sample_size','time_to_sort', marker='.')     
g = g.map(plt.plot , 'sample_size','time_to_sort', marker='.', linestyle = ':').add_legend()     