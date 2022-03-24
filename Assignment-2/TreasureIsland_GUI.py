''' MODULE FOR THE TREASURE HUNTING ISLAND GUI PROGRAM '''


from tkinter import Tk, Canvas, Label, Button, messagebox
from PIL import ImageTk, Image
from itertools import count
from pygame import mixer


class ImageLabel(Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)

        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


def restart(root, ask='No'):
    if ask == 'Yes':
        if messagebox.askokcancel("Quit", "Do you want to Restart? All your progress would be lost."):
            mixer.music.stop()
            root.destroy()
            treasureIsland_GUI()
    else:
        mixer.music.stop()
        root.destroy()
        treasureIsland_GUI()

def on_exit(root):
    if messagebox.askokcancel("Quit", "Do you want to quit the Game?"):
        mixer.music.stop()
        root.destroy()

def load_animation(root, image_path, text):
    root.destroy()
    root = Tk()

    root.title('Treasure Island GUI')
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f'{w}x{h}')
    root.state('zoomed')

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load(image_path)

    Label(root, text=text).place(anchor='center', x=root.winfo_screenwidth() / 2, y=root.winfo_screenheight() - 100)
    Button(root, text='RESTART', command=lambda: restart(root, 'Yes')).place(anchor='ne', x=90, y=40)
    Button(root, text='EXIT GAME', command=lambda: on_exit(root)).place(anchor='nw', x=root.winfo_screenwidth() - 90, y=40)

    root.mainloop()

def play_sound(path2audio_file, loop = False):
    mixer.init()
    mixer.music.load(path2audio_file)
    if loop:
        mixer.music.play(loops=-1)
    else:
        mixer.music.play(loops=0)
    return mixer.music

def door_choice(root, text, image_path):
    print(f'\n{text}')
    if text != 'You Win!':
        play_sound("RSS/Audios/Treasure Island GUI Audios/Lost Audio.wav")
    else:
        play_sound("RSS/Audios/Treasure Island GUI Audios/Win Audio.mp3")
    load_animation(root, image_path, text)

def wait_choice(root, can):
    Label(can, text='Which door?').place(anchor='n', relx=1 / 4, rely=0.6)
    Button(can, text='Red', command=lambda: door_choice(root, 'Burned by fire.\nGame Over.', "RSS/Images/Treasure Island GUI Images/Fire.gif")).place(anchor='n', relx=5 / 32, rely=0.7)
    Button(can, text='Yellow', command=lambda: door_choice(root, 'You Win!', "RSS/Images/Treasure Island GUI Images/Win.gif")).place(anchor='n', relx=7 / 32, rely=0.7)
    Button(can, text='Blue', command=lambda: door_choice(root, 'Eaten by beasts.\nGame Over.', "RSS/Images/Treasure Island GUI Images/Beast.gif")).place(anchor='n', relx=9 / 32, rely=0.7)
    Button(can, text='Others', command=lambda: door_choice(root, 'Game Over.',  "RSS/Images/Treasure Island GUI Images/Over.gif")).place(anchor='n', relx=11 / 32, rely=0.7)

def swim_or_other_choices(root, text, image_path):
    print(f'\n{text}')
    play_sound("RSS/Audios/Treasure Island GUI Audios/Lost Audio.wav")
    load_animation(root, image_path, text)

def left_choice(root, can):
    Label(can, text='swim or wait').place(anchor='n', relx=1/3, rely=0.4)
    Button(can, text='Wait', command=lambda: wait_choice(root, can)).place(anchor='n', relx=1 / 4, rely=0.5)
    Button(can, text='Swim', command=lambda: swim_or_other_choices(root, 'Attacked by Trout.\nGame Over.', "RSS/Images/Treasure Island GUI Images/Trout.gif")).place(anchor='n', relx=1 / 3, rely=0.5)
    Button(can, text='Others', command=lambda: swim_or_other_choices(root, 'Attacked by Trout.\nGame Over.', "RSS/Images/Treasure Island GUI Images/Trout.gif")).place(anchor='n', relx=5 / 12, rely=0.5)

def right_or_other_choices(root, text, image_path):
    print(f'\n{text}')
    play_sound("RSS/Audios/Treasure Island GUI Audios/Lost Audio.wav")
    load_animation(root, image_path, text)

def start(root, can):
    play_sound("RSS/Audios/Treasure Island GUI Audios/BGM.mp3", True)
    Label(can, text='left or right?').place(anchor='n', relx=0.5, rely=0.2)
    Button(can, text='Left', command=lambda: left_choice(root, can)).place(anchor='n', relx=1/3, rely=0.3)
    Button(can, text='Right', command=lambda: right_or_other_choices(root, 'Fall into a hole.\nGame Over.', "RSS/Images/Treasure Island GUI Images/Hole.gif")).place(anchor='n', relx=0.5, rely=0.3)
    Button(can, text='Others', command=lambda: right_or_other_choices(root, 'Fall into a hole.\nGame Over.', "RSS/Images/Treasure Island GUI Images/Hole.gif")).place(anchor='n', relx=2/3, rely=0.3)


def treasureIsland_GUI():
    root = Tk()
    root.title('Treasure Island GUI')
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f'{w}x{h}')
    root.state('zoomed')

    can = Canvas(root, width=w, height=h)

    img = ImageTk.PhotoImage(Image.open("RSS/Images/Treasure Island GUI Images/Bg Img.jpg").resize((w, h)))
    can.background = img
    can.create_image(0, 0, anchor='nw', image=img)

    Label(can, text='Welcome to Treasure Island.\nYour mission is to find the treasure.').place(anchor='n', x=w / 2, y=20)

    Button(can, text='RESTART', command=lambda: restart(root, 'Yes')).place(anchor='nw', x=20, y=20)

    Button(can, text='EXIT GAME', command=lambda: on_exit(root)).place(anchor='ne', x=w - 20, y=20)

    Button(can, text='START', command=lambda: start(root, can)).place(anchor='n', relx=0.5, rely=0.1)


    root.protocol("WM_DELETE_WINDOW", lambda: on_exit(root))
    can.pack()
    root.mainloop()


