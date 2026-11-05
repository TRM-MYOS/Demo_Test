def add(a: int, b: int) -> int:
    assert isinstance(a, int)
    return a + b


if __name__ == "__main__":
    print(add(2, 3))