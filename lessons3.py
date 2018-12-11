import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize
import math

def f(x):
    return math.sin(x/5.0)*math.exp(x/10.0) + 5*math.exp(-x/2.0)
    
x = np.arange(1, 31, 0.01)
y = map(f, x)
plt.plot(x, y)
