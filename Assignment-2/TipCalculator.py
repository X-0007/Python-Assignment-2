''' MODULE FOR THE RESTAURANT TIP CALCULATOR PROGRAM '''

def tipCalculator():
    print('Welcome to the tip Calculator.')
    total_bill = float(input('What was the total bill in INR? '))

    def getTip(total_bill):
        percentage_tip = int(input('What percentage of tip would you like to give? 10, 12 or 15?\n'))
        if percentage_tip in (10, 12, 15):
            diner_count = int(input('How many people to split the bill? '))
            print('Each person should pay in INR?', round(((1 + 0.01 * percentage_tip) * total_bill) / diner_count, 2))
        else:
            print('Whoops! Please Enter a Valid Tip Amount! Choose among 10, 12 or 15 in INR.\nPlease try again...')
            getTip(total_bill)

    getTip(total_bill)


