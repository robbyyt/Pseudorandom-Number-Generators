import random_utils

bit_output = ""
LENGTH = 2 ** 16

p = random_utils.get_usable_prime(1.34078e154)
q = random_utils.get_usable_prime(1.34078e154)

N = p * q
seed = random_utils.get_random_integer()
x = (seed ** 2) % N

for contor in range(LENGTH):
    x = (x ** 2) % N
    bit_result = str(x % 2)
    bit_output += bit_result

print "OUTPUT:\n" + bit_output
random_utils.print_statistics(bit_output)
