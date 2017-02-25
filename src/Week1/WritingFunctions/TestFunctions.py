def ones_digit(n):
    return abs(n) % 10


def test_ones_digit():
    print("Testing ones_digit()...", end="")
    assert(ones_digit(5) == 5)
    assert(ones_digit(123) == 3)
    assert(ones_digit(100) == 0)
    assert(ones_digit(999) == 9)
    assert(ones_digit(-125) == 5)
    print("Passed!")

test_ones_digit()

