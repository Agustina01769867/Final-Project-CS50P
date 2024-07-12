from project import calcular_beta1, calcular_beta0, get_csv
import pytest
from urllib.error import HTTPError


A = [1, 2, 3, 4, 5, 6, 7, 8]
B = [2, 3, 4, 5, 6, 7, 8, 9]


def test_beta1():
    assert calcular_beta1(A, B) == 1


def test_beta0():
    assert calcular_beta0(A, B, calcular_beta1(A, B)) == 1


def test_get_csv():
    with pytest.raises(SystemExit):
        assert get_csv("CS50")

