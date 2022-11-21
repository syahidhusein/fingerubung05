import math
import numpy as np



def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    for i in range(num_iterations):
        id_max = values.index(max(values))
        if id_max == (len(values)-1):
            values[id_max-1] = values[id_max-1] + share*(max(values))
            values[0] = values[0] + share*(max(values))
            values[id_max] = values[id_max] - 2*share*(max(values))
        elif id_max == 0:
            values[-1] = values[-1] + share*(max(values))
            values[id_max+1] = values[id_max+1] + share*(max(values))
            values[id_max] = values[id_max] - 2*share*(max(values))
        else:
            values[id_max-1] = values[id_max-1] + share*(max(values))
            values[id_max+1] = values[id_max+1] + share*(max(values))
            values[id_max] = values[id_max] - 2*share*(max(values))
    print(values)
    return

fair_sharer([0, 1000, 800, 0], 2)

