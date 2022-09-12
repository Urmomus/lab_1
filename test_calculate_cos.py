from math import cos, isclose

import pytest
from calculate_cos import calculate_cos


def test_calculate_cos_ok():
    assert isclose(calculate_cos(4, 0.001).final_value, cos(4), rel_tol=0.001)
    assert isclose(calculate_cos(18, 10e-11).final_value, cos(18), rel_tol=10e-11)


def test_calculate_cos_negative_number():
    with pytest.raises(ValueError):
        calculate_cos(12, -7)

    with pytest.raises(ValueError):
        calculate_cos(13, 0)
