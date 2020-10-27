import pytest 
from calculator import *
import numpy as np 
import math



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