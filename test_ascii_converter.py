#import pytest
import numpy as np
from ascii_converter import min_max_scaling

def test_min_max_scaling():
    test_array = np.arange(0,11)
    array_scaled = min_max_scaling(test_array)
    assert np.min(array_scaled) == 0
    assert np.max(array_scaled) == 1
    array_expected = np.arange(0,1.1,0.1)
    #assert np.all(array_expected == array_scaled)
    assert np.allclose(array_scaled,array_expected)
    
def test_min_max_scaling_nzMin():
    test_array = np.arange(10,241)
    array_scaled = min_max_scaling(test_array)
    assert np.min(array_scaled) == 0
    assert np.max(array_scaled) == 1