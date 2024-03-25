from main import QbitN
import numpy as np

def toffoli(control1, control2, target):
  identity = np.eye(2)

  cnot = np.kron(identity, np.array([[1, 0], [0, 1]]))
  cnot[3, 1] = 1
  cnot[7, 5] = 1

  cswap_control1 = np.eye(8)
  cswap_control1[control1 * 4 : (control1 + 1) * 4, control1 * 4 : (control1 + 1) * 4] = 0
  cswap_control1[control1 * 4 : (control1 + 1) * 4, target * 4] = np.array([1, 0, 1, 0])
  cswap_control1[target * 4, control1 * 4 : (control1 + 1) * 4] = np.array([1, 0, 1, 0])

  cswap_control2 = np.eye(8)
  cswap_control2[(control2 + 1) * 4 : , (control2 + 1) * 4 : ] = 0
  cswap_control2[(control2 + 1) * 4 : , target * 4 + 2] = np.array([1, 0, 1, 0])
  cswap_control2[target * 4 + 2, (control2 + 1) * 4 : ] = np.array([1, 0, 1, 0])

  QbitN[control1, control2, target] = np.dot(np.dot(cswap_control2, np.dot(cnot, cswap_control1)), identity)
