import Factors


def primeNumbers(start, stop):
    primes = []
    for i in range(start, stop + 1):
        if Factors.findFactors(i) == [-i, -1, 1, i]:
            primes.append(i)
    return primes


