import numpy as np
from scipy.misc import derivative
import math

__all__ = ['softmax']

def softmax(X):
    """
    This function returns the softmax value for the given input
    """
    if len(X) > 1:
        expo = np.exp(X)
        expo_sum = np.sum(np.exp(X))
        ret = expo/expo_sum
        print(f'The softmax result on the given input {ret}')
        return ret
    else:
        raise ValueError("Sorry, lenght of the list should be more than one") 
        
def get_derivative(fn,x):
    der = derivative(fn,x,dx=1e-9)
    return der

def softmax_derivative(x):
    """
    This function returns the softmax derivative value for the given input
    """
    der = derivative(softmax,x,dx=1e-9)
    return der



    