import pytest 
from calculator import *
import numpy as np 
import math
from calculator import derivative


def test_cos():
    round(cos(9),2) == round(math.cos(9),2)

def test_sin():
    round(sin(9),2) == round(math.sin(9),2)

def test_tan():
    round(tan(9),2) == round(math.tan(9),2)

def test_tanh():
    round(tanh(9),2) == round(np.tanh(9),2)

def test_sigmoid():
    round(sigmoid(9),2) > 0.5

def test_ReLU():
    round(relu(9.54531),2) == 9.55

def test_e():
    round(e(1),2) == 2.71 

def test_log():
    round(log(5),2) == 1.61

def test_softmax():
    softmax([2,3]) == [0.26894142, 0.73105858]


# def test_softmax_1():
#     with pytest.raises(ValueError) as e_info:
#         softmax([2]) == 'Exception: Sorry, lenght of the list should be more than one'

def test_cos_derivative():
    round(derivative.cos_derivative(5),2) == 0.96

def test_sin_derivative():
    round(derivative.sin_derivative(5),2) == 0.28

def test_e_derivative():
    round(derivative.e_derivative(5),2) == 148.41

def test_log_derivative():
    round(derivative.log_derivative(5),2) == 0.2

def test_relu_derivative():
    round(derivative.relu_derivative(5),2) == 1.0

    