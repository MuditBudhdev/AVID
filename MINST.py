import numpy as np
def MINST(hex):
    bias = -5
    first = hex * 5 + bias
    normalized_out = sigmoid(first)
    if normalized_out < 0.3:
        print("this pixel has black")
    else:
        print("this pixel is not black")





def sigmoid(output):
    sigmoid = 1 / (1 + np.exp(-output))
    return sigmoid

MINST(0.8)