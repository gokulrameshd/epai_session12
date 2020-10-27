import math 
from scipy.misc import derivative


def cos(args):
    """
    This function returns the cosine value of the given input
    """
    ret = math.cos(args)
    return ret

def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der
