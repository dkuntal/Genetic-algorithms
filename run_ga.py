import numpy as np
import math

import generate
import crossover
import mutation
import fitness

bin_small_file = "files/bin_small.txt"
bin_pop_file = "files/bin_pop.txt"
off_file = "files/bin_pop_off.txt"
fit_file = "fitness.txt"
n_ivar = 75
pop_size = int(4)
sol_size = 20
ivar_file = "test/ivar.txt"
dvar_file = "test/dvar.txt"
wt_file = "test/wt.txt"
generations = 2
fact = 10
neg_fact = 0
exp_fact = 100
cp = 0.2
mp = 0.01

def pop_ivars_dvar(bin_pop_file,ivar_file,dvar_file):
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
#     print(dvar)
    return pop, ivars, dvar







def run_ga(bin_pop_file,ivar_file,dvar_file,n_ivar,pop_size,generations,fact,neg_fact,exp_fact):
    
    fit_file_write = open(fit_file,'w')
    mindiff = 9999999999
    
    for i_gen in range(generations):
        print('gen',i_gen)
        pop, ivars, dvar = pop_ivars_dvar(bin_pop_file,ivar_file,dvar_file)

