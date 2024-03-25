import numpy as np
from main import QbitN

def m(i):
    state = QbitN[i]
    normalized_state = state / np.linalg.norm(state)
    
    probabilities = np.abs(normalized_state) ** 2
    outcome = np.random.choice(len(state), p=probabilities)
    
    QbitN[i] = outcome
