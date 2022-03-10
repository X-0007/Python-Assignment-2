### Here, I've tried demonstrating most of the Approaches for finding Factorial using Functions, which I could think of. ###

from PrimeNumbers import primeNumbers
from math import factorial
from functools import reduce
from operator import add, pow

def factorialByBuiltInFunction(n):
    return factorial(n)


def factorialByPrimeFactors(n):
    def primeFactorisation(num):
        prime_factors = primeNumbers(1, n)
        powers = []
        for i in range(len(prime_factors)):
            quotient, count = num, 0
            while quotient % prime_factors[i] == 0:
                quotient /= prime_factors[i]
                count += 1
            powers.append(count)
        return {'prime_factors': prime_factors, 'powers': powers}

    powers_sum = primeFactorisation(2)['powers']

    for i in range(3, n + 1):
        powers_sum = list(map(add, powers_sum, primeFactorisation(i)['powers']))

    return reduce(lambda x, y: x * y, list(map(pow, primeFactorisation(1)['prime_factors'], powers_sum)))


def factorialUsingReduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


def factorialBySplitRec(N):
    def rec_product(start, stop):
        numfactors = (stop - start) >> 1
        if numfactors == 2: return start * (start + 2)
        if numfactors > 1:
            mid = (start + numfactors) | 1
            return rec_product(start, mid) * rec_product(mid, stop)
        if numfactors == 1: return start
        return 1

    inner = outer = 1

    for i in range(len(bin(N).lstrip('-0b')), -1, -1):
        inner *= rec_product((N >> i + 1) + 1 | 1, (N >> i) + 1 | 1)
        outer *= inner
    n = N - ((N >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    n = (((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24
    return outer << (N - n)


def factorialByRecursion(n):
    return 1 if n in (0, 1) else factorialByRecursion(n - 1) * n


def factorialByIteration(n):
    factorial, i = 1, 2
    while i != n + 1:
        factorial *= i
        i += 1
    return factorial


