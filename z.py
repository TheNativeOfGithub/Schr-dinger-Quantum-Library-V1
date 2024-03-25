from main import QbitN
import numpy as np

def z(i):
    QbitN[i] = np.array([[1, 0],
                   [0, -1]])