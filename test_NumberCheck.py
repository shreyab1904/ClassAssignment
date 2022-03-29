import NumberCheck
import pytest

@pytest.fixture
def input():
    a=101
    return a

@pytest.mark.parametrize("num,output",[(2,True),(101,True),(202,False)])
def test_prime(num,output):
    result=NumberCheck.prime(num)
    assert result==output

@pytest.mark.parametrize("num,output",[(101,True),(201,False)])
def test_palindrome(num,output):
    result=NumberCheck.palindrome(num)
    assert result==output