import pandas as pd
#'pandas' allow us to manage data, work on data and do some statistic,
#  goes hand by hand with an other
# import 'numpy' that is used for calcules and usally iported together
import numpy as np


## 1 dimentional data type -- .Series
# similiar to list but different work of index
lst = [1,2,3,4]
s = pd.Series(lst)
print (s[2])
# we can change index instead of classic list 0,1,2,3...
myindex = ['s1', 's2', 's3', 's4']
sw1 = pd.Series(lst, index= myindex)
print(sw1['s1'])

randoms = pd.Series(np.random.randn(4), index=myindex)
# Creating a new Series with index of myindex that has as
# element random numbers called with np.random

data = {'s1': 12, 's2': 8, 's3': 4, 's4': 6}
sdict = pd.Series(data)
# Can also create a Series in one step using dictionary whose keys will became our indx
