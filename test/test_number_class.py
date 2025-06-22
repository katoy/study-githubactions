import pytest
from number_class import NumberHolder

def test_number_holder():
    number_holder = NumberHolder(5, 10)
    num1, num2 = number_holder.get_numbers()
    assert num1 == 5
    assert num2 == 10

def test_number_holder_with_negative():
    number_holder = NumberHolder(-1, 0)
    num1, num2 = number_holder.get_numbers()
    assert num1 == -1
    assert num2 == 0

def test_number_holder_with_zero():
    number_holder = NumberHolder(0, 0)
    num1, num2 = number_holder.get_numbers()
    assert num1 == 0
    assert num2 == 0

def test_number_holder_with_large_numbers():
    number_holder = NumberHolder(1000000, 2000000)
    num1, num2 = number_holder.get_numbers()
    assert num1 == 1000000
    assert num2 == 2000000

def test_number_holder_with_invalid_input():
    with pytest.raises(TypeError):
        NumberHolder("a", 1)

def test_number_holder_with_invalid_num2():
    with pytest.raises(TypeError):
        NumberHolder(1, "b")
