import pytest
import calculator
from calculator import *


def test_add():
    assert add(4,5) == 9

def test_subtract():
    assert subtract(6,2) == 4

def test_multiply():
    assert multiply(2,11) == 22

def test_div():
    assert divide(10,2) == 5

@pytest.mark.parametrize("num1,num2,expectedRes", [(8,1,9),(3,4,7),(12,1,13)])
def test_param_add(num1,num2,expectedRes):
    result = calculator.add(num1,num2)
    assert result == expectedRes


@pytest.mark.parametrize("num1,num2,expectedRes", [(8,2,6),(3,4,-1),(12,6,6)])
def test_param_subtract(num1,num2,expectedRes):
    result = calculator.subtract(num1,num2)
    assert result == expectedRes

@pytest.mark.parametrize("num1,num2,expectedRes", [(1,2,2),(3,4,12),(5,6,30)])
def test_param_multi(num1,num2,expectedRes):
    result = calculator.multiply(num1,num2)
    assert result == expectedRes


@pytest.mark.parametrize("num1,num2,expectedRes", [(1,2,0.5),(8,4,2),(50,5,10)])
def test_param_divide(num1,num2,expectedRes):
    result = calculator.divide(num1,num2)
    assert result == expectedRes