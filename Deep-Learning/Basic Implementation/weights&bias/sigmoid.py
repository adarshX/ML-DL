# ANN
#2 input nuerons, 1 hidden layer with 1 nueron , 1 output nueron
#Activation function is sigmoid function
#inputs  -- x1,x2
#weights -- w1,w2
#Bias -- b1

import numpy as np
import math
import matplotlib.pyplot as plt
x1 = np.linspace(-10,10,num=21 )  #input can be any point of this set
x2 = np.linspace(-10,10,num=21 )

def sigmoid(x):
	f = 1 / (1 + math.exp(-x))
	return f

w1 = 1 
w2 = 2
n_b = 3
b1 = np.linspace(-10,10,num=n_b) #bias of hidden node
print(b1)
sum = []
for i in range(n_b):
	s = w1 * x1 + w2 * x2 + b1[i]
	sum.append(s)



a =  [[0 for j in range(21)] for i in range(n_b)] 	#activation functn values  
for i in range(n_b):			#iterating for each bias
	for j in range(21):		# finding function values for diff inputs
		a[i][j] = sigmoid(sum[i][j])

fig1 = plt.figure()
for i in range(n_b):
	plt.plot(sum[i],a[i])

fig1.suptitle('Sigmoid function(3 diff bias)', fontsize=10)
plt.show()



