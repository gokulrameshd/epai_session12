import math
from scipy.misc import derivative

__all__ = ['log']

def log(args):
    """
    This function returns the log value for the given input
    """
    ret  = math.log(args)
    return ret


def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der

def log_derivative(x):
    der = derivative(log,x,dx=1e-9)
    return der