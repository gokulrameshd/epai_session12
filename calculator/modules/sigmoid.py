import math
import numpy as np 
from scipy.misc import derivative

__all__ = ['sigmoid']

def sigmoid(X):
    """
    This function returns the sigmoid value for the given input
    """
    return 1/(1+np.exp(-X))

def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der

def sigmoid_derivative(x):
    der = derivative(sigmoid,x,dx=1e-9)
    return der