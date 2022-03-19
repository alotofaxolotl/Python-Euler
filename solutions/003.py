# https://projecteuler.net/problem=3
# What is the largest prime factor of the number 600851475143?
import primes
from math import sqrt

n = 600851475143

for i in range(1, int(sqrt(n)) + 1, 2):
    if n % i == 0:
        if primes.is_prime(i):
            print(i)
