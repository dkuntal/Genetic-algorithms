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
pop_size = int(100)
sol_size = 20
ivar_file = "test/ivar.txt"
dvar_file = "test/dvar.txt"
wt_file = "test/wt.txt"
generations = 2
fact = 10
neg_fact = 0
exp_fact = 12000
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

def calc_fitness(pop_size,ivars,n_ivar,pop,dvar,fact,neg_fact,exp_fact,sol_size):
    fits = []
    diffs = []
    for i in range(pop_size):
    #     print(dvar[i])
        fit = []
        diff = []
        ivar = []
        ivar_ = ivars[i].split(' ')
        for k in range(sol_size):
            for j in range(n_ivar):
        #         print(ivar_)
        #         print(ivar_[j])
                ivar.append(int(ivar_[j]))
            fit_, diff_ = fitness.expo_fit(pop[i],ivar,float(dvar[i]),fact,neg_fact,exp_fact)
            fit.append(fit_)
            diff.append(diff_)
        diffs.append(np.sum(diff))
        fits.append(np.prod(fit))
        
    try:
        del ivar, ivar_
    except:
        pass
    return fits,diffs

def sel_prob(fit,pop_size):
    prob = []
    for i in range(pop_size):
        prob.append(fit[i]/sum(fit))
    return prob

def cu_prob(fit,pop_size):
    cuprob = []
    temp = 0
    for i in range(pop_size):
        temp += fit[i]/sum(fit)
        cuprob.append(temp)
    del temp
    return cuprob

def roul_wheel_sel(pop,cuprob,n_offsp):
    offsp = []
    for i in range(n_offsp):
        r = np.random.random()
        for j in range(len(pop)):
            
            off = pop[len(pop)-1]
            if r < cuprob[j]:
                off = pop[j]
                break
        offsp.append(off)
    return offsp












def run_ga(bin_pop_file,ivar_file,dvar_file,n_ivar,pop_size,generations,fact,neg_fact,exp_fact):
    
    fit_file_write = open(fit_file,'w')
    mindiff = 9999999999
    
    for i_gen in range(generations):
        print('gen',i_gen)
        pop, ivars, dvar = pop_ivars_dvar(bin_pop_file,ivar_file,dvar_file)

        fit,diff = calc_fitness(pop_size,ivars,n_ivar,pop,dvar,fact,neg_fact,exp_fact,sol_size)

run_ga(bin_pop_file,ivar_file,dvar_file,n_ivar,pop_size,generations,fact,neg_fact,exp_fact)
