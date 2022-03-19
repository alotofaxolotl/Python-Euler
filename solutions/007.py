# https://projecteuler.net/problem=7
# What is the 10 001st prime number?

import primes

n = 10001
p = 1
while n > 1:
    p += 2
    if primes.is_prime(p):
        n -= 1

print(p)