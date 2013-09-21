import math
import random
import sys
import mcmc

#Enter the input data, here it is x and corresponding y values.
x_data = []
y_data = []
input_data = open(sys.argv[1])          #input is a tab separated file containing data
for line in input_data:
    data = line.split('\t')
    x_data.append(int(data[0]))
    y_data.append(int(data[1]))


#range of parameters [[min, mean, max, standard_deviation] for each parameter]
parameter_range = [[5.0,0.0,10.0,0.1],[10.0,0.0,20.0,0.1]]
numberofparameters = 2


#generating initial point
parametersi = []
for i in range(numberofparameters):
	parameterini = parameter_range[i][1] + random.random() * (parameter_range[i][2] - parameter_range[i][1])
	parametersi.append(parameterini)	#initial point for each parameter

#initial function value	
ini_fun_value = mcmc.fitness_function(x_data, y_data, parametersi)


#choose the features for the mcmc
iterations = 100
step = 1.0
burn_in = 0.0
results_mcmc = mcmc.metropolis(x_data, y_data, iterations, parametersi, ini_fun_value, parameter_range,step, burn_in)
print results_mcmc
