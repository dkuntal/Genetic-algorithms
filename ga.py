import math
import numpy as np
from IPython import get_ipython

import generate
# import crossover
# import mutation
import fitness

bin_small_file = "files/bin_small.txt"
bin_pop_file = "files/bin_pop.txt"
n_ivar = 75
pop_size = 100
ivar_file = "test/ivar.txt"
dvar_file = "test/dvar.txt"

# generate small binary-------------------------------++
generate.gen_all_save(bin_small_file,7)

# generate population---------------------------------++
generate.gen_pop(bin_small_file,bin_pop_file,n_ivar,pop_size)

inp = open(bin_pop_file,'r')
pop = inp.read().split('\n')
inp.close()

# inval
inp = open(ivar_file,'r')
ivars = inp.read().split('\n')
inp.close()

# dependent variable
inp = open(dvar_file,'r')
dvar = inp.read().split('\n')
# print(dvar)
inp.close()
try:
    del inp
except:
    pass
    
# calculate fitness-----------------------------------
fit = []
for i in range(pop_size):
#     print(dvar[i])
    ivar = []
    ivar_ = ivars[i].split(' ')
    for j in range(n_ivar):
#         print(ivar_)
#         print(ivar_[j])
        ivar.append(int(ivar_[j],pop_size))
    fit.append(fitness.expo_fit(instr=pop[i],inval=ivar,rval=float(dvar[i]),fact=1,neg_fact=0,exp_fact=10000))
try:
    del ivar, ivar_
except:
    pass
print(fit)
# print(sum(fit))

# probability of selection----------------------------
prob = []
for i in range(pop_size):
    prob.append(fit[i]/sum(fit))
print(prob)

# cumulative probability of selection-----------------
cuprob = []
temp = 0
for i in range(pop_size):
    temp += fit[i]/sum(fit)
    cuprob.append(temp)
del temp
print(cuprob)

# loop---------------------------------
#     roulet wheel random
#     select offspring
# crossover
# mutation
