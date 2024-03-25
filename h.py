from main import QbitN
import numpy as np
from numpy import sqrt

def h(i):
    QbitN[i] = np.array([[1/sqrt(2), 1/sqrt(2)],
                     [1/sqrt(2), -1/sqrt(2)]])