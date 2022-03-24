''' MODULE FOR THE RESTAURANT CLI PROGRAM '''


from tkinter import Tk, Frame, Label, Text, Button
from PIL import Image, ImageTk


def calculate(tbs):
    def num(n):
        try:
            if float(n) == int(n):
                return int(n)
        except (Exception,):
            try:
                return float(n)
            except (Exception,):
                print('Invalid Input/Types! Please try again...')
                tbs[3].delete('1.0', 'end')
                tbs[3].insert('end', 'Invalid Input/Type! Please try again...')
    txts = [num(tb.get(1.0, 'end - 1c')) for tb in tbs[: -1]]
    if isinstance(txts[0], (int, float)) and txts[0] >= 0 and txts[1] in (10, 12, 15) and isinstance(txts[2], int) and txts[2] > 0:
        tbs[3].delete('1.0', 'end')
        tbs[3].insert('end', round(((1 + 0.01 * txts[1]) * txts[0]) / txts[2], 2))
        print('Each person should pay in INR?', tbs[3].get('1.0', 'end'))

def clear(tbs):
    [tb.delete('1.0', 'end') for tb in tbs]

def reset(root):
    root.destroy()
    tipCalculator_GUI()

def tipCalculator_GUI():
    root = Tk()
    root.title('Restaurant Tip Calculator')
    root.geometry(f'800x600-{1900 - root.winfo_screenwidth()}-{1000 - root.winfo_screenheight()}')
    fr = Frame(root)

    logo_img = Image.open("RSS/Images/Restaurant Tip Calculator Images/Restaurant Logo.jpg").resize((100, 100))
    logo_im = ImageTk.PhotoImage(logo_img)


    lb_logo = Label(fr, image=logo_im)
    lb_logo.configure(image=logo_im)
    lb_logo.image = logo_im

    tip_calculator = Label(fr, text='Welcome to the tip Calculator.')

    lb_total_bill = Label(fr, text='What was the total bill in INR? ')
    tb_total_bill = Text(fr, width=25, height=1)

    lb_percentage_tip = Label(fr, text='What percentage of tip would you like to give? 10, 12 or 15?')
    tb_percentage_tip = Text(fr, width=25, height=1)

    lb_diner_count = Label(fr, text='How many people to split the bill? ')
    tb_diner_count = Text(fr, width=25, height=1)

    btn_calculate = Button(fr, text='CALCULATE', command=lambda: calculate([tb_total_bill, tb_percentage_tip, tb_diner_count, tb_bill_share_pay]))

    lb_bill_share_pay = Label(fr, text='Each person should pay in INR? ')
    tb_bill_share_pay = Text(fr, width=25, height=1)

    btn_clear = Button(fr, text='CLEAR', command=lambda: clear([tb_total_bill, tb_percentage_tip, tb_diner_count, tb_bill_share_pay]))

    btn_reset = Button(fr, text='RESET', command=lambda: reset(root))

    btn_exit = Button(fr, text='EXIT', command=root.destroy)



    fr.place(anchor='center', relx=0.5, rely=0.5)

    lb_logo.grid(row=0, column=1, pady=20)

    tip_calculator.grid(row=1, column=1, pady=20)

    lb_total_bill.grid(row=2, column=0, pady=20)
    tb_total_bill.grid(row=2, column=2, pady=20)

    lb_percentage_tip.grid(row=3, column=0, pady=20)
    tb_percentage_tip.grid(row=3, column=2, pady=20)

    lb_diner_count.grid(row=4, column=0, pady=20)
    tb_diner_count.grid(row=4, column=2, pady=20)

    btn_calculate.grid(row=5, column=1, pady=20)

    lb_bill_share_pay.grid(row=6, column=0, pady=20)
    tb_bill_share_pay.grid(row=6, column=2, pady=20)

    btn_clear.grid(row=7, column=0, pady=20)
    btn_reset.grid(row=7, column=1, pady=20)
    btn_exit.grid(row=7, column=2, pady=20)


    root.mainloop()


