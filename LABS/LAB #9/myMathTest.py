
from myMath import add, divide

def test_add(a,b):
    assert add(1 + 3) == 4 
    assert add(5 + 39) == 44
    assert add(-43 + 27) == -16 
    assert add (60 + 7) == 67
    return(a,b)

