
# coding: utf-8

# In[3]:

import math
import random
import numpy as np


# In[6]:

def bin_mu0(inp_,pm):
    inp = int(inp_,10)
#     len = int(math.log10(inp_))+1
    len1 = len(inp_)
    for j in range(0,len1):
#         print(j+1)
#         if random.random() < pm:
        if np.random.uniform() < pm:
#             j = i-1
            a = round(inp/(10**(j+1)))*(10**(j+1))
            b = inp%(10**j)
            c = inp-a-b
#             print('a',a)
#             print('b',b)
#             print('c',c)
            if c == 0:
                c = 10**j
            else:
                c = 0
#             print('c',c)
            inp = a+c+b
            
#             print(j+1,inp)
#         print('------------------------')
    return inp


# In[17]:

def bin_mu(inp_,pm):
#     len = int(math.log10(inp_))+1
    len1 = len(inp_)
    inp = list(inp_)
    out = ''
    for j in range(len1):
        if np.random.uniform() < pm:
            if inp[j] == '1':
                out += '0'
            else:
                out += '1'
#             print(j+1,out)
        else:
            out += inp[j]
            
#             print(j+1,inp)
#         print('------------------------')
#     print(out)
    return out


# In[16]:

# x = '000110011001'
# bin_mu(x,.5)
