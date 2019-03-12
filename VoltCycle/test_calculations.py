import numpy as np
import pandas as pd

import calculations

def test_peak_potentials():
    """This function tests get_peak_potentials() function."""
    data = {'potential': [0.167, 0.251, 0.500], 'current': [-46.370, 33.153, 7.040]}
    df = pd.DataFrame(data)
    index = np.array([0, 1])
    potential_column_name = 'potential'
    assert type(calculations.peak_potentials(df, index, potential_column_name)) == np.ndarray, "output is not an array"
    assert calculations.peak_potentials(df, index, potential_column_name)[0] == 0.167, "array value incorrect for data"
    assert calculations.peak_potentials(df, index, potential_column_name)[1] == 0.251, "array value incorrect for data"
    return

def test_half_wave_potential():
    """This function tests half_potentials() function."""
    data = {'potential': [0.167, 0.251, 0.500], 'current': [-46.370, 33.153, 7.040]}
    df = pd.DataFrame(data)
    index = np.array([0, 1])
    potential_column_name = 'potential'
    assert type(calculations.half_wave_potential(df, index, potential_column_name)) == np.float64, "output data type not a float"
    np.testing.assert_almost_equal(calculations.half_wave_potential(df, index, potential_column_name), ((0.251-0.167)/2), decimal=3)
    return