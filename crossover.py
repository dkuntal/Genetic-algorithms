
# coding: utf-8

# In[1]:

import math
import random
import numpy as np


# In[91]:

def cross(inp1,inp2,cp):
    cp = max(1,cp)
    out1 = inp1[:cp-1]+inp2[cp-1:]
    out2 = inp2[:cp-1]+inp1[cp-1:]
#     print(inp1,inp2)
#     print(out1,out2)
#     print(cp)
    return out1,out2


# In[92]:

def bin_sp_cross(inp1_,inp2_,pc):
    len1 = len(inp1_)
    inp1 = int(inp1_,10)
    inp2 = int(inp2_,10)
    cp = np.random.randint(low=1, high=len1)
    cpTrue = False
#     dir = np.random.uniform(-1,+1)
#     print(cp, dir)
#     while dir == 0.0:
#         dir = np.random.uniform(-1,+1)
#     print(cp, dir)
    while cpTrue != True:
        r = np.random.uniform()
#         print(r)
        if r < pc:
            break
#         cp += np.sign(dir)
        cp += 1
        cp = cp%len1
    
#     print(cp)
    return cross(inp1_,inp2_,cp)


# In[106]:

def bin_mp_cross(inp1_,inp2_,pc):
    len1 = len(inp1_)
    inp1 = int(inp1_,10)
    inp2 = int(inp2_,10)
    cp = []
    for i in range(len1):
#         if np.random.uniform() < pc:
        r = np.random.uniform()
        print(r)
        if r < pc:
#             cp.append(i+1)
            inp1_, inp2_ = cross(inp1_,inp2_,i+1)
            print(i+1,inp1_,inp2_)
    return(inp1_, inp2_)
#     print(cp)


# In[93]:

# print(bin_sp_cross('12345678','00000000',0.1))


# In[107]:

# print(bin_mp_cross('12345678','00000000',0.4))
