import io
import pytest

from matrix_multiplier import matrix_multiplier
from obtain_input import obtain_input_mat

# used this reference https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html


def test_matrix_multiplier_1():

    m1 = [[1, 0], [0, 1]]
    m2 = [[1, 0], [0, 1]]
    r = matrix_multiplier(m1, m2)
    assert r == [[1, 0], [0, 1]]


def test_matrix_multiplier_1_1():

    m1 = [[1, 1], [1, 1]]
    m2 = [[1, 1], [1, 1]]
    r = matrix_multiplier(m1, m2)
    assert r == [[2, 2], [2, 2]]


def test_matrix_multiplier_2():

    m1 = [[1, 2], [3, 4]]
    m2 = [[1, 2], [3, 4]]
    r = matrix_multiplier(m1, m2)
    assert r == [[7, 10], [15, 22]]


def test_good_matrix_input(monkeypatch):
    """
    Verify that proper integer input is accepted.
    """

    # monkeypatch the "sys.stdin", so that it returns
    # matrix dimensions and values (all separated by new line)
    stdin = io.StringIO("2\n2\n1\n2\n3\n4\n")
    monkeypatch.setattr('sys.stdin', stdin)

    # go about using input() like you normally would
    # it uses sys.stdin under the hood:
    m = obtain_input_mat()
    assert m == [[1, 2], [3, 4]]


def test_bad_matrix_input(monkeypatch):
    """
    Verify that non integer input is not accepted.
    """

    # monkeypatch the "sys.stdin", so that it returns
    # matrix dimensions and values (all separated by new line)
    stdin = io.StringIO("2\n2\n1\nd\n3\n4\n")
    monkeypatch.setattr('sys.stdin', stdin)

    # go about using input() like you normally would
    # it uses sys.stdin under the hood:
    with pytest.raises(ValueError) as exc_info:
        m = obtain_input_mat()
    # assert exc_info.value.args[0] == 'some info'
    assert str(exc_info.value) == 'some info'
