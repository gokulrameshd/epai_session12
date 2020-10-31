import numpy as np
from scipy.misc import derivative
import math


__all__ = ['e']

def e(X):
    """
    This function returns the e value for the given input
    """
    expo = np.exp(X)
    return expo

def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der

def e_derivative(x):
    der = derivative(e,x,dx=1e-9)
    return der