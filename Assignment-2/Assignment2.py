''' MAIN PYTHON FILE FOR CARRYING OUT ALL THE ASSIGNEMENT TASKS IN THE FORM OF AN INFINITE LOOPING CLI MENU SEQUENCE '''

# An Infinite Rolling CLI Menu Sub-Sequence has also been provided for User's attraction, attention and ease. #
# The program has also been made robust enough to cope-up and handle the Uncheked Exceptions generating. #



from MagicWordGenerator import magicWordGenerator
from TipCalculator import tipCalculator
from TreasureIsland import treasureIsland
from RockPaperScissorsGame import RPS_Game
from MagicWordGenerator_GUI import magicWordGenerator_GUI
from TipCalculator_GUI import tipCalculator_GUI
from TreasureIsland_GUI import treasureIsland_GUI
from RockPaperScissorsGame_GUI import RPS_Game_GUI


class Assignment2:
    def getChoice(self):
        print('\n' * 2 + '\t' * 5 + ' ' * 3 + '* ' * 11 + '*')
        print('\t' * 4 + ' ' * 6 + '* ' * 5 + ' ' + '\033[4mMENU\033[0m' + ' ' + ' *' * 4 + ' *')
        print('\t' * 5 + ' ' * 3 + '* ' * 11 + '*')
        print('\t' + '* ' * 32)
        print('\t* *' + ' *' * 30)
        print('\t' + '* ' * 2 + '\t' * 14 + '* *')
        print('\t' + '* ' * 2 + '\t' * 5 + ' ' * 3 + '\033[4mCLI Apps\033[0m' + '\t' * 6 + ' ' * 3 + ' *' * 2)
        print("\t" + "* " * 2 + "  [+] Enter '1' for the Magic Word Generator." + " " * 10 + " *" * 2)
        print("\t" + "* " * 2 + "  [+] Enter '2' for the Restaurant Tip Calculator." + " " * 5 + " *" * 2)
        print("\t" + "* " * 2 + "  [+] Enter '3' for the Treasure Hunting Island." + " " * 7 + " *" * 2)
        print("\t" + "* " * 2 + "  [+] Enter '4' for the Rock, Paper, Scissors Game." + " " * 4 + " *" * 2)
        print('\t' + '* ' * 2 + '\t' * 14 + '* *')
        print('\t' + '* ' * 2 + '\t' * 14 + '* *')
        print('\t' + '* ' * 2 + '\t' * 5 + ' ' * 3 + '\033[4mGUI Apps\033[0m' + '\t' * 6 + ' ' * 3 + ' *' * 2)
        print("\t" + "* " * 2 + "  [+] Enter '5' for the Magic Word Generator GUI." + " " * 6 + " *" * 2)
        print("\t" + "* " * 2 + "  [+] Enter '6' for the Restaurant Tip Calculator GUI." + " " + " *" * 2)
        print("\t" + "* " * 2 + "  [+] Enter '7' for the Treasure Island GUI." + " " * 11 + " *" * 2)
        print("\t" + "* " * 2 + "  [+] Enter '8' for the Rock, Paper, Scissors GUI Game." + " *" * 2)
        print('\t' + '* ' * 2 + '\t' * 14 + '* *')
        print('\t' + '* ' * 2 + '\t' * 14 + '* *')
        print("\t" + "* " * 2 + "  [-] Press '0' to Exit the Menu." + " " * 22 + " *" * 2)
        print('\t' + '* ' * 2 + '\t' * 14 + '* *')
        print('\t* *' + ' *' * 30)
        print('\t' + '* ' * 32 + '\n' * 2)
        print('Provide the operations you want to perform...')
        choice = int(input('Enter your choice: '))
        return choice

    def MagicWordGenerator(self):
        magicWordGenerator()

    def TipCalculator(self):
        tipCalculator()

    def TreasureIsland(self):
        treasureIsland()

    def Rock_Paper_Scissors(self):
        RPS_Game()

    def Magic_Word_Generator_GUI(self):
        magicWordGenerator_GUI()

    def Tip_Calculator_GUI(self):
        tipCalculator_GUI()

    def TreasureIsland_GUI(self):
        treasureIsland_GUI()

    def Rock_Paper_Scissors_GUI(self):
        RPS_Game_GUI()



def main():
    obj = Assignment2()
    while True:
        choice = obj.getChoice()
        print()
        if choice == 0:
            return
        elif choice in (1, 2, 3, 4, 5, 6, 7, 8):
            if choice == 1:
                obj.MagicWordGenerator()
            elif choice == 2:
                obj.TipCalculator()
            elif choice == 3:
                obj.TreasureIsland()
            elif choice == 4:
                obj.Rock_Paper_Scissors()
            elif choice == 5:
                obj.Magic_Word_Generator_GUI()
            elif choice == 6:
                obj.Tip_Calculator_GUI()
            elif choice == 7:
                obj.TreasureIsland_GUI()
            else:
                obj.Rock_Paper_Scissors_GUI()
        else:
            print('Oops! Invalid Choice! Please try again...')
            main()


if __name__ == '__main__':
    try:
        main()
    except (Exception, ):
        print('\nInvalid Choice/Type/Format of Input! Please try again...')
        main()




