import math
import numpy as np 


def relu(X):
    """
    This function returns the relu value for the given input
    """
    return np.maximum(0,X)