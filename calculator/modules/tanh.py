import math 
from scipy.misc import derivative
import numpy as np


__all__ = ['tanh']


def tanh(args):
    """
    This function returns the tanh value for the given input
    """
    ret = np.tanh(args)
    return ret

def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der

def tanh_derivative(x):
    der = derivative(tanh,x,dx=1e-9)
    return der