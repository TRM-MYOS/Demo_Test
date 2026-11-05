def add(a: int, b: int) -> int:
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert a >= 0
    assert b >= 0
    assert a <= 1000
    assert b <= 1000
    assert a + b <= 2000
    return a + b


if __name__ == "__main__":
    print(add(2, 3))