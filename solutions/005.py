# https://projecteuler.net/problem=5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 20
t = n * n
found = False

while not found:
    found = True
    for i in range(11, n):
        if t % i != 0:
            found = False
            t += n
            break

print(t)