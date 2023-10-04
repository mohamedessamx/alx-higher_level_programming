#!/usr/bin/python3
def print_alphabet_reverse():
    for i in range(ord('z'), ord('A') - 1, -1):
        print("{:c}".format(i), end="")
