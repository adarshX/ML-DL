## Training process

**Forward propagation**:
* Neurons store data in input layer --- > transmitted to hidden layer neurons ---> transfer to the 
output layer and that is output 
* From each layer, information is transferred through channels. ---> these have weights(weighted channel)
* Each neuron of the hidden layer has certain no. called bias.
* Bias is added to the weighted sum coming into that neuron from the previous layer
* This above sum is applied to an activation function.
* This function decides whether a neuron is activated or not.
* Each activated neuron passes info to the next layer till the last hidden layer. 
* This last hidden layer goes to neurons of output layers.
* If the output layer’s neuron is activated, then that particular output neuron represents the correct form of our raw input data.
* The **neuron in output layers with the highest values(Probability) determines the output**.
* This is called forward propagation.

**Backward propagation**:
* During forward propagation , if the neuron with wrong input has the highest probability, then we use back propagation algo.
* After each forward propagation, you calculate the error between actual and desired output.  
* Now you traverse from your output layer to hidden layers(backward), and update(change) your weights such that your error in next forward propagation is less.
* The weights are updated based on the current forward propagation error.
* This is iteratively done until you have less error(correct prediction)

* This cycle of forward and backward propagation is called as training process.
* After your learning process is completed, you get the desired output with highest probability.

