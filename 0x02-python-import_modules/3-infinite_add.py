#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
from sys import argv
add = 0
for s in argv[1:]:
    add += int(s)
print("{:d}".format(add))
