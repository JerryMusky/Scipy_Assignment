# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:44:57 2023

@author: Pei Ren
"""

from scipy.optimize import minimize
import numpy as np

def objective_fcn(x):
    return -((x[3]*x[6]*0.063)-(x[0]*5.04 + x[1]*0.035 + x[2]*10/1000 + x[4]*3.36))
    #To maximize profits

#Defining equations
#Equation 8
def LinInequlity_constraint1 (x):
    return (35.82 - 0.222*x[9]) - 0.99*x[8] 

#Equation 9
def LinInequlity_constraint2 (x):
    return -(35.82 - 0.222*x[9]) + (100/99)*x[8] 

#Equation 10
def Linequlity_constraint3 (x):
    return (-133 + 3*x[6]) - 0.99*x[9] 

#Equation 11
def Linequlity_constraint4 (x):
    return -(-133 + 3*x[6]) + (100/99)*x[9] 

#Equation 1 
def Linequality_constraint1 (x):
    return x[4] - 1.22*x[3] + x[0] 

#Equation 4
def NLInequality_constraint1 (x):
    return (x[0]*(1.12 + 0.13167*x[7] - 0.0067*x[7]**2)) - 0.99*x[3] 

#Equation 5 
def NLInequality_constraint2 (x):
    return -(x[0]*(1.12 + 0.13167*x[7] - 0.0067*x[7]**2)) + (100/99)*x[3]

#Equation 6
def NLInequality_constraint3 (x):
    return (86.35 + 1.098*x[7] - 0.038*x[7]**2 + 0.325*(x[5] - 89)) - 0.99*x[6] 

#Equation 7
def NLInequality_constraint4 (x):
    return -(86.35 + 1.098*x[7] - 0.038*x[7]**2 + 0.325*(x[5] - 89)) + (100/99)*x[6] 

#Equation 2
def NLequality_constraint1 (x):
    return (x[5]*x[3]*x[8]) + (1000*x[2]*x[5]) - (98000*x[2])

#Equation 3
def NLequality_constraint2 (x):
    # return x[7] - ((x[1]+x[4]) / x[0])
    return (x[7]*x[0]) - x[1] - x[4] 
    

bound = ((0,2000),      #bound_x1
         (0,16000),     #bound_x2 
         (0,120000),    #bound_x3
         (0,5000),      #bound_x4
         (0,2000),      #bound_x5
         (85,93),       #bound_x6
         (90,95),       #bound_x7
         (3,12),        #bound_x8
         (1.2,4),       #bound_x9
         (145,162))     #bound_x10



#sample equality constraint = {'type': 'eq', 'fun': equality_constraint}
#sample inequality constraint = {'type': 'ineq', 'fun': inequality_constraint}


#Equation 8
constraint1 = {'type': 'ineq', 'fun': LinInequlity_constraint1}

#Equation 9
constraint2 = {'type': 'ineq', 'fun': LinInequlity_constraint2}

#Equation 10
constraint3 = {'type': 'ineq', 'fun': Linequlity_constraint3}

#Equation 11
constraint4 = {'type': 'ineq', 'fun': Linequlity_constraint4}

#Equation 1
constraint5 = {'type': 'eq', 'fun': Linequality_constraint1}

#Equation 4
constraint6 = {'type': 'ineq', 'fun': NLInequality_constraint1}

#Equation 5
constraint7 = {'type': 'ineq', 'fun': NLInequality_constraint2}

#Equation 6 
constraint8 = {'type': 'ineq', 'fun': NLInequality_constraint3}

#Equation 7
constraint9 = {'type': 'ineq', 'fun': NLInequality_constraint4}

#Equation 2
constraint10 = {'type': 'eq', 'fun': NLequality_constraint1}

#Equation 3
constraint11 = {'type': 'eq', 'fun': NLequality_constraint2}

constraint = (constraint1, constraint2, constraint3, constraint4, constraint5,
constraint6, constraint7, constraint8, constraint9, constraint10, constraint11)


lower_bounds = [0, 0, 0, 0, 0, 85, 90, 3, 1.2, 145]
upper_bounds = [2000, 16000, 12000, 5000, 2000, 93, 95, 12, 4, 162]
x0 = np.random.uniform(lower_bounds, upper_bounds, size= (1,10))
#creating random x1-x10 integer to start off

option = {'maxiter': 1000, 'disp': True}

result = minimize(objective_fcn, x0, method = 'SLSQP', bounds = bound, 
                  constraints = constraint, options=option)

print(result)
