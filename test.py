import numpy as np
def neuron(freeNum, linkNum, attachNum):
    bias = -3
    first = freeNum * 1
    second = linkNum * 3 
    third  = attachNum * 4 
    output = (first) + second + third + bias
    normalized_output = sigmoid(output)
    if normalized_output > 0.5:
        print("this is a spam")
    else:
        print("this is not spam")


def sigmoid(output):
    sigmoid = 1 / (1 + np.exp(-output))
    return sigmoid


neuron(1,0,0)