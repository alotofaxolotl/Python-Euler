from math import sqrt

def is_prime(p):
    if p == 2: return True
    if p % 2 == 0: return False
    for i in range(3, int(sqrt(p)) + 1, 2):
        if p % i == 0: return False
    return True