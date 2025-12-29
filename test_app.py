from app import add, divide
import pytest

def test_add():
    assert add(a=3, b=3) == 6

def test_divide():
    assert divide(a=6, b=3) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(a=1, b=0)
