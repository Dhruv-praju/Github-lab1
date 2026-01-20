import pytest
from src import calculator

def test_add():
    assert calculator.add(2,3) == 5
    assert calculator.add(5,0) == 5
    assert calculator.add(-1,1) == 0
    assert calculator.add(-4, -3) == -7

def test_subract():
    assert calculator.subract(3, 2) == 1
    assert calculator.subract(2, -3) == 5
    assert calculator.subract(2, 2) == 0
    assert calculator.subract(-2, -5) == 3

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, -7) == 7
    assert calculator.multiply(0, 4) == 0
    assert calculator.multiply(2, -4) == -8

def test_add_all():
    assert calculator.add_all(3, 4, 5) == 12
    assert calculator.add_all(-1, 2, -1) == 0
    assert calculator.add_all(-5, 20, 20) == 35
    assert calculator.add_all(-5, -1, -5) == -11