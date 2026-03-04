from main import add

def test_add_correct():
    assert add(2, 2) == 4

def test_add_negative():
    assert add(-1, -1) == -2
