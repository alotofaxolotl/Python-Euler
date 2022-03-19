# https://projecteuler.net/problem=4
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palendrome(n: int) -> bool:
    n_str = str(n)
    head = 0
    tail = len(n_str) - 1
    while(head <= tail):
        if n_str[head] != n_str[tail]:
            return False
        head += 1
        tail -= 1
    return True


palendromes = []
a = 999
while(a > 0):
    b = 999
    while(b > 0):
        product = a * b
        if is_palendrome(product):
            palendromes.append(product)
        b -= 1
    a -= 1

palendromes.sort(reverse=True)
print(palendromes[0])