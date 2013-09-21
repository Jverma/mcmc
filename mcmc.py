import math
import random




#define the fitness function, here it is a straight line.   
def fitness_function(x, y, parameters):
    a = parameters[0]
    b = parameters[1]
    chi2 = 0.0
    for i in range(len(x)):
        y_new = a*x[i] + b
        chi2 = chi2 + ((y_new - y[i]/(y[i]*0.5)))**2
    return chi2/len(x)



####################################################################
#DON'T CHANGE BELOW THIS
#####################################################################
def metropolis(x_data, y_data, iterations, ini_parameters, ini_fun_value, parameter_range, step_size, burn_in):
    alpha = []
    for i in range(iterations):
        accepted_points = 0
        new_parameters = []
        for j in range(len(ini_parameters)):
            param = ini_parameters[j] + random.gauss(0.0, 1.0)*parameter_range[j][3]*step_size
            new_parameters.append(param)
        new_fun_value = fitness_function(x_data, y_data, new_parameters)
        posterior = new_fun_value/ini_fun_value
        if (posterior > random.random()):
            accepted_points +=1
            accepted_ratio = float(accepted_points/(i + 1))
            ini_parameters = [x for x in new_parameters]
            ini_fun_value = new_fun_value
            if (accepted_points > burn_in):
                alpha.append(ini_parameters)        
    return alpha       
                
