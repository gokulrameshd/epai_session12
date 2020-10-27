import numpy as numpy

import math

def softmax(X):
    """
    This function returns the soft value for the given input
    """
    expo = np.exp(X)
    expo_sum = np.sum(np.exp(X))
    return expo/expo_sum