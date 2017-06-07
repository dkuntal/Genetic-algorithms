
# coding: utf-8

# In[1]:

import math
import numpy as np
import itertools


# In[2]:

def all_bin(len1):
    s = '1'*len1
#     print(s)
    s += '0'*len1
#     print(len(s),s)
    return s


# In[3]:

def gen_all(filename,len1):
#     for f in itertools.combinations([1,0],len):
#         print(f)
    s = all_bin(len1)
    l = list(itertools.permutations(s,len1))
    l1 = []
    for i in range(0,len(l)):
        l1.append(''.join(l[i]))
    return set(l1)


# In[15]:

def gen_all_save(filename,len1):
    output = open(filename,"w")
    s = gen_all(filename,len1)
    for i in s:
        output.write(i+'\n')
    output.close()


# In[2]:

def gen_pop(infile_name,outfile_name,n,pop_size):
    infile = open(infile_name,'r').read()
    bins = infile.split('\n')
    outfile = open(outfile_name,'w')
    for i in range(pop_size):
        for j in range(n):
#             p = np.random.randint(len(bins)-1)
#             print(i,j,p,bins[p])
            outfile.write(bins[np.random.randint(len(bins)-1)])
#             if bins[p] == '':
#                 j -= 1
            if j < n-1:
                outfile.write(' ')
        outfile.write('\n')


# In[16]:

gen_all_save("files/bin_small.txt",7)


# In[23]:

gen_pop("files/bin_small.txt","files/bin_str.txt",75,10)


# In[ ]:


