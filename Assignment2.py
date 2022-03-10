''' MAIN PYTHON FILE FOR CARRYING OUT ALL THE ASSIGNEMENT TASKS IN THE FORM OF AN INFINITE LOOPING CLI MENU SEQUENCE '''
# The program has also been made robust enough to cope-up and handle the Uncheked Exceptions generating #


from MagicWordGenerator import magicWordGenerator
from TipCalculator import tipCalculator
from TreasureIsland import treasureIsland
from RockPaperScissorsGame import RPS_Game


class Assignment2:
    def getChoice(self):
        print('\n' * 2 + '\t' * 5 + ' ' * 3 + '* ' * 11 + '*')
        print('\t' * 4 + ' ' * 6 + '* ' * 5 + ' ' + 'MENU' + ' ' + ' *' * 4 + ' *')
        print('\t' * 5 + ' ' * 3 + '* ' * 11 + '*')
        print('\t' + '* ' * 30)
        print('\t* *' + ' *' * 28)
        print('\t' + '* ' * 2 + '\t' * 8 + '\t' * 5 + '* *')
        print("\t" + "* " * 2 + "  [-] Press '0' to Exit the Menu." + " " * 18 + " *" * 2)
        print("\t" + "* " * 2 + "  [+] Enter '1' for the Magic Word Generator." + " " * 6 + " *" * 2)
        print("\t" + "* " * 2 + "  [+] Enter '2' for the Restaurant Tip Calculator." + " " + " *" * 2)
        print("\t" + "* " * 2 + "  [+] Enter '3' for the Treasure Hunting Island." + " " * 3 + " *" * 2)
        print("\t" + "* " * 2 + "  [+] Enter '4' for the Rock, Paper, Scissors Game." + " *" * 2)
        print('\t' + '* ' * 2 + '\t' * 8 + '\t' * 5 + '* *')
        print('\t* *' + ' *' * 28)
        print('\t' + '* ' * 30 + '\n' * 2)
        print('Provide the operations you want to perform...')
        choice = int(input('Enter your choice: '))
        return choice

    def MagicWordGenerator(self):
        magicWordGenerator()

    def TipCalculator(self):
        tipCalculator()

    def TreasureIsland(self):
        treasureIsland()

    def Rock_Paper_Scissor(self):
        RPS_Game()



def main():
    obj = Assignment2()
    while True:
        choice = obj.getChoice()
        print()
        if choice == 0:
            return
        elif choice in (1, 2, 3, 4):
            if choice == 1:
                obj.MagicWordGenerator()
            elif choice == 2:
                obj.TipCalculator()
            elif choice == 3:
                obj.TreasureIsland()
            elif choice == 4:
                obj.Rock_Paper_Scissor()
        else:
            print('Oops! Invalid Choice! Please try again...')
            main()


if __name__ == '__main__':
    try:
        main()
    except (Exception, ):
        print('\nInvalid Choice/Type/Format of Input! Please try again...')
        main()




