import math 
from scipy.misc import derivative


def cos(args):
    ret = math.cos(args)
    return ret

def get_derivative(fn):
    der = derivative(fn,5.0,dx=1e-9)
    return der
