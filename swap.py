from main import QbitN

def swap(i, x):
    temp = {}
    temp.update(QbitN[i])
    QbitN[i] = 0 + QbitN[x]
    QbitN[x] = 0 + temp[0]
    del temp[0]