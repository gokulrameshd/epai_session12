import math
import numpy as np 
from scipy.misc import derivative


__all__ = ['relu']

def relu(X):
    """
    This function returns the relu value for the given input
    """
    return np.maximum(0,X)


def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der

def relu_derivative(x):
    der = derivative(relu,x,dx=1e-9)
    return der