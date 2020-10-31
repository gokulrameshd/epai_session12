import math 
from scipy.misc import derivative


__all__ = ['sin']

def sin(args):
    """
    This function returns the sine value of the given input
    """
    ret = math.sin(args)
    return ret

def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der

def sin_derivative(x):
    der = derivative(sin,x,dx=1e-9)
    return der