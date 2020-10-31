import numpy as numpy
from scipy.misc import derivative
import math

__all__ = ['softmax']

def softmax(X):
    """
    This function returns the soft value for the given input
    """
    expo = np.exp(X)
    expo_sum = np.sum(np.exp(X))
    return expo/expo_sum


def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der

def softmax_derivative(x):
    der = derivative(softmax,x,dx=1e-9)
    return der

    