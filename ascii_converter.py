import numpy as np

def min_max_scaling(array):
    """Scales all values in array by the min and max value.
    """
    min_value = np.min(array)
    max_value = np.max(array)
    return (array- min_value)/(max_value - min_value)

