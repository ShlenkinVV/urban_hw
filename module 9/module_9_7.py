"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV

Декораторы
"""


def is_prime(func):
    def wrapper(a, b, c):
        prime = 'Простое'
        res = func(a, b, c)
        if res <= 1:
            prime = 'Составное'
        else:
            for i in range(2, int(res ** 0.5) + 1):
                if res % i == 0:
                    prime = 'Составное'
        print(prime)
        return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

result = sum_three(2, 3, 1)
print(result)
