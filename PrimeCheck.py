import Factors


def checkPrime(n):
    return True if Factors.findFactors(n) == [-n, -1, 1, n] else False


