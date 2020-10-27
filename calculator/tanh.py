import math 
from scipy.misc import derivative
import numpy as np

def tanh(args):
    """
    This function returns the tanh value for the given input
    """
    ret = np.tanh(args)
    return ret