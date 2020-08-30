#Note : This script outputs most accurate ouput by having below weights & bias 
#        No itertation and optimisation are used.        
# XOR gate
# 2 input nodes , 2 hidden nodes , 1 output node
#input nodes numbering = 1,2
#hidden nodes numbering = 1,2
#ouput nodes numbering = 1

import numpy as np
import math

input = [(0,0),(1,0),(0,1),(1,1)]  #input array
y = [0,1,1,0]                      #expected_output  array


# case : (1,0) -> 1


def sigmoid(x):
	f = 1 / (1 + math.exp(-x))
	return f


x1 = 1 
x2 = 0

#weights(w_ij) of input node(i) with hidden node(j)
w11  = 5
w12  = 10
w21  = 15
w22  = 20

#biases of hidden nodes
b1 = -4
b2 = -8

#sums
S1 = w11 * x1 + w21 * x2 + b1
S2 = w12 * x1 + w22 * x2 + b2

z1 = sigmoid(S1)
z2 = sigmoid(S2)

##weights(wo_ij) of hidden node(i) with ouput node(j)
wo_11 = 6
wo_21 = 10

#biases of ouput nodes
bo_1 = 8

#sums
So_1 = wo_11 * z1 + wo_21 * z2 + bo_1


y_p = sigmoid(So_1)
print(y_p)

error = 1 - y_p
error = error * 100
print(error)
