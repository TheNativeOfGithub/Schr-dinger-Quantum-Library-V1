from main import QbitN
import numpy as np

def cnot(i, x):
  cnot = np.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 1],
                   [0, 0, 1, 0]])

  cswap = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
  cswap[QbitN[i], QbitN[i]] = 0
  cswap[QbitN[i], QbitN[x]] = 1
  cswap[QbitN[x], QbitN[i]] = 1

  QbitN[i, x] = np.dot(cswap, np.dot(cnot, cswap))
