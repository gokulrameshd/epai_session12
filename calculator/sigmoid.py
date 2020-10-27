import math
import numpy as np 


def sigmoid(X):
    """
    This function returns the sigmoid value for the given input
    """
    return 1/(1+np.exp(-X))

