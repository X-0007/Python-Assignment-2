import Factorials
import Factors
import PrimeCheck
import PrimeNumbers

class Assignment1:
    def getChoices(self):
        print('\t' + '* ' * 30)
        print('\t* *' + ' *' * 28)
        print("\t" + "* " * 2 + " [-] Press '0' to Exit." + "\t" * 8 + "* *")
        print("\t" + "* " * 2 + " [+] Enter '1' for calculating the Factorial." + "\t" * 2 + "* *")
        print("\t" + "* " * 2 + " [+] Enter '2' for finding the Factors." + "\t" * 4 + "* *")
        print("\t" + "* " * 2 + " [+] Enter '3' for checking for Prime." + "\t" * 4 + "* *")
        print("\t" + "* " * 2 + " [+] Enter '4' for finding Prime Numbers upto 100.  * *")
        print('\t* *' + ' *' * 28)
        print('\t' + '* ' * 30 + '\n')
        print('Provide the operations you want to perform...')
        choices = (input("Enter your choice(s)[Delimeters either comma ',' or space ' ']: "))
        choices = choices.split(',') if choices.find(',') != -1 else choices.split(' ')
        return list(dict.fromkeys(map(lambda x: int(x), choices)))

    def getOptions(self):
        choices = self.getChoices()
        ' '.join([str(i) for i in choices])
        if str(choices).find('0') != -1:
            print("\nOption '0' Inputed! Exiting...")
            return
        else:
            for i in choices:
                if i not in [0, 1, 2, 3, 4, ' ']:
                    print('Oops! Invalid Input. Please try again...\n')
                    self.getOptions()
                else:
                    return choices

    def getFactors(self, n):
        return Factors.findFactors(n)

    def getPrimes(self, start, stop):
        return PrimeNumbers.primeNumbers(start, stop)

    def findFactorial(self, n):
        return Factorials.factorialByIteration(n)

    def isPrime(self, n):
        return PrimeCheck.checkPrime(n)

    def performOperation(self, opt):
        print()
        if opt == 4:
            res = self.getPrimes(0, 100)
            print('>> Prime Numbers upto 100 are:', end = ' ', sep = ', ')
            print(*res, sep = ', ')
        else:
            if opt == 1:
                n = int(input('>> Please Enter the Number whose Factorial you want to Calculate: '))
                res = self.findFactorial(n)
                print(f'The Factorial of {n} is', str(res))
            elif opt == 2:
                n = int(input('>> Please Enter the Number whose Factors(+ve/-ve) you want to Find: '))
                res = self.getFactors(n)
                print(f'The Factors(+ve/-ve) of {n} are:', end = ' ')
                print(*res, sep = ', ')
            else:
                n = int(input('>> Please Enter the Number you want to check for Prime: '))
                res = self.isPrime(n)
                print(f'Yes, {n} is a Prime Number!') if res else print(f'No, {n} is not a Prime Number!')

def main():
    try:
        while True:
            obj = Assignment1()
            print('\n' + '\t' * 5 + ' ' * 3 + '* ' * 11 + '*')
            print('\t' * 4 + ' ' * 6 + '* ' * 5 + ' ' + 'MENU' + ' ' + ' *' * 4 + ' *')
            print('\t' * 5 + ' ' * 3 + '* ' * 11 + '*')
            inputs = obj.getOptions()
            if inputs is None:
                return
            else:
                for i in inputs:
                    obj.performOperation(i)
    except (Exception,):
        print('Invalid Choice/Type/Format of Input! Please try again...')
        main()


if __name__ == '__main__':
    main()


