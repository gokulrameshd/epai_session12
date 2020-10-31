import math 
from scipy.misc import derivative

__all__ = ['tan']

def tan(args):
    """
    This function returns the tan value for the given input
    """
    ret = math.tan(args)
    return ret

def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der

def tan_derivative(x):
    der = derivative(tan,x,dx=1e-9)
    return der