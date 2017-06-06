
# coding: utf-8

# In[1]:

import math
import numpy as np


# In[8]:

def predict(instr,inval,fact,neg_fact):
    # instr = input string with ' '
    # inva
    strs = instr.split(' ')
    len1 = len(strs[0])
    maxval = 2**(len1-1)
    
#     vals = []
    out = 0
    for i in range(len(strs)):
#         vals.append(int(strs[i],2))
#         out += vals[i]*inval[i]
#         ival = int(inval[i],2)
        temp = int(strs[i],2)
#         out += (temp-maxval*neg_fact)*inval[i]/fact
        out += (temp-maxval*neg_fact)*inval[i]/fact
    return out


# In[ ]:

# def inv_fit(m):
    


# In[ ]:

def sub_fit(instr,inval,rval,):
    diff = abs(rval - predict(instr,inval,fact,neg_fact))


# In[2]:

def expo_fit(instr,inval,rval,fact,neg_fact,exp_fact):
    diff = abs(rval - predict(instr,inval,fact,neg_fact))
#     print(diff)
#     print(math.exp((-1)*diff/exp_fact))
    return math.exp((-1)*diff/exp_fact), diff
#     return e


# In[7]:

# instr = 
# expo_fit()
