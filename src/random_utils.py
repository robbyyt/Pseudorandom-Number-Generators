import random
import sympy
import sys
from collections import Counter


def get_usable_prime(upper_bound):
    current_prime = sympy.randprime(0, upper_bound + 1)

    while current_prime % 4 != 3:
        current_prime = sympy.randprime(0, upper_bound + 1)

    return current_prime


def print_statistics(bitstring):
    bit_frequencies = Counter(bitstring)
    print "Statistics:"
    for i in bit_frequencies:
        print "Percentage of " + i + ": " + str((bit_frequencies[i] * 100) / len(bitstring)) + "%"


def get_random_integer():
    return random.randint(0, sys.maxint)
