import numpy as np

def adding(x,y):
    z = x+y
    if type(x) == list and type(y) == list:
        z = np.array(x) + np.array(y)
    return z

def sort_list(l):
    sl = np.sort(l)
    return sl

