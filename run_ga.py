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
