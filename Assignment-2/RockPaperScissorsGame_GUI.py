''' MODULE FOR THE ROCK, PAPER, SCISSORS GUI GAME '''


from tkinter import Tk, Label, Text, Frame, Button
from PIL import Image, ImageTk
from random import randint


def response(root, header, tb, player_choice):
    computer_choice = randint(0, 2)
    computer_choice_image = ['Rock', 'Paper', 'Scissors']

    img = Image.open(f"./RSS/RPS_IMGS/RPS_{computer_choice_image[computer_choice]}.jpg").resize((200, 300))
    im = ImageTk.PhotoImage(img)

    header.configure(image=im)
    root.header = Label(root, image=im)
    header.label = im
    header.pack()

    tb.delete(1.0, 'end')
    choice_dict = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
    print(f"\nYou chose: {choice_dict[player_choice]}\nComputer's choice: {choice_dict[computer_choice]}")
    if player_choice == computer_choice:
        tb.insert('end', "It's a tie. Can try again...")
        print("It's a tie. Can try again...")
    elif str(player_choice) + str(computer_choice) in ('02', '10', '21'):
        tb.insert('end', 'HURRAY! You Won!!')
        print('HURRAY! You Won!!')
    else:
        tb.insert('end', 'OOPS! You Lose. Try again...')
        print('OOPS! You Lose. Try again...')
    tb.pack()

def restart(root):
    print('\nRestarting the Game...')
    root.destroy()
    RPS_Game_GUI()

def RPS_Game_GUI():
    root = Tk()
    root.title('Rock, Paper, Scissors Game')
    root.geometry(f'800x600-{1900 - root.winfo_screenwidth()}-{1000 - root.winfo_screenheight()}')

    title = Label(text="COMPUTER'S CHOICE :")

    img = Image.open("RSS/RPS_IMGS/RPS.jpg").resize((200, 300))
    im = ImageTk.PhotoImage(img)


    header = Label(root, image=im)
    header.label = im


    tb = Text(root, width=30, height=1)


    control_panel = Frame(root)


    frame_head = Label(control_panel, text='CONTROLS:', justify='center')


    l0 = Label(control_panel, text='Rock: ')

    b0 = Button(control_panel, text='0', width=3, command=lambda: response(root, header, tb, 0))

    l1 = Label(control_panel, text='Paper: ')

    b1 = Button(control_panel, text='1', width=3, command=lambda: response(root, header, tb, 1))

    l2 = Label(control_panel, text='Scissors: ')

    b2 = Button(control_panel, text='2', width=3, command=lambda: response(root, header, tb, 2))


    reset = Button(control_panel, text='RESTART', width=6, command=lambda: restart(root))

    Exit = Button(control_panel, text='EXIT', width=6, command=root.destroy)



    title.pack()
    control_panel.pack(side='bottom')
    frame_head.grid(row=0, column=3, padx=16, pady=16)
    l0.grid(row=1, column=1, padx=16, pady=16)
    b0.grid(row=1, column=2, padx=8, pady=16)
    l1.grid(row=1, column=3, padx=16, pady=16)
    b1.grid(row=1, column=4, padx=8, pady=16)
    l2.grid(row=1, column=5, padx=16, pady=16)
    b2.grid(row=1, column=6, padx=8, pady=16)
    reset.grid(row=2, column=3, padx=8, pady=16)
    Exit.grid(row=2, column=4, padx=8, pady=16)

    root.mainloop()


