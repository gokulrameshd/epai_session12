import math 
from scipy.misc import derivative


__all__ = ['cos']

def cos(args):
    """
    This function returns the cosine value of the given input
    """
    ret = math.cos(args)
    return ret

def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der

def cos_derivative(x):
    """
    This function returns the cosine derivative value of the given input
    """
    der = derivative(cos,x,dx=1e-9)
    return der