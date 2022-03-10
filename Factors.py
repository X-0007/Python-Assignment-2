from math import floor, sqrt


def findFactors(n):
    if isinstance(n, int):
        if n == 0 or n == 1:
            return [1]
        facts = [1]
        for i in range(2, floor(sqrt(n) + 1)):
            if n % i == 0:
                facts.append(i)
        facts = list(dict.fromkeys(facts + [(n // i) for i in facts[-1::-1]]))
        return list(map(lambda x: -x, facts[::-1])) + facts
    else:
        print('Invalid Input! Please Input a Valid Whole Number.')
        return


