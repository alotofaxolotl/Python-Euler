# https://projecteuler.net/problem=2
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.

sum = 0

a = 0
b = 1

while(b < 4000000):
    c = a + b
    a = b
    b = c

    if b % 2 == 0:
        sum += b

print(sum)