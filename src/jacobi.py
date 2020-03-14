import random_utils

"""
def compute_jacobi(a, n):
    b = a % n
    c = n
    s = 1
    while b >= 2:
        while b % 4 == 0:
            b /= 4

        if b % 2 == 0:
            if c % 8 == 3 or c % 8 == 5:
                s = -s
            b = b / 2

        if b == 1:
            break

        if b % 4 == 3 and c % 4 == 3:
            s = -s
            (b, c) = (c % b, b)

    return s * b
"""


def compute_jacobi(a, n):
    assert (n > a > 0 and n % 2 == 1)
    s = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                s = -s
        a, n = n, a
        if a % 4 == n % 4 == 3:
            s = -s
        a %= n
    if n == 1:
        return s
    else:
        return 0


bit_output = ""
p = random_utils.get_usable_prime(1.34078e154)
q = random_utils.get_usable_prime(1.34078e154)
LENGTH = 2 ** 16
N = p * q
seed = random_utils.get_random_integer() % N

for i in range(LENGTH):
    jacobi = compute_jacobi(seed + i + 1, N)
    bit_result = (jacobi + 1) / 2
    bit_output += str(bit_result)

print "OUTPUT:\n" + bit_output
random_utils.print_statistics(bit_output)
