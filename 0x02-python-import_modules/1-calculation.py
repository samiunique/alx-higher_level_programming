#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, add(a, b)))
    print("{} * {} = {}".format(a, b, add(a, b)))
    print("{} / {} = {}".format(a, b, add(a, b)))
