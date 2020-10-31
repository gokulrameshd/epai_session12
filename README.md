# epai_session12

In This assignment , The task is to 

- Create modules which contains the functions for  sin, cos, tan, tanh, SoftMax, Sigmoid, ReLU, log and e and also for their derivatives.

- When the calculator is imported then it has to import 
sin, cos, tan, tanh, SoftMax, Sigmoid, ReLU, log and e  and not their derivatives.

- When we use *"from calculator import derivative"* it has to import the all the derivative functions



Directory/Code Structure:

calculator
 |-__init__.py
 |-cos.py
 |-e.py
 |-log.py
 |-ReLU.py
 ......

 * Within the calulator directory all the modules are placed
 * __all__ is used achieve the problem statement. This helps us over power the funtion of ** "import *" **
 * This __init__.py file import the functions from the modules
 * The derivative file imports all the derivative functions.





