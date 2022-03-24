''' MODULE FOR THE MAGIC WORD GENERATOR GUI PROGRAM '''


from tkinter import Tk, Frame, Label, Text, Button
from PIL import Image, ImageTk
from SearchImages import getImages
from random import choice


path2key = "./RSS/PVT_RS/pvt.txt"

def magic(fr, city_name, pet_or_movie_name, lb_city_image, lb_pet_or_movie_image, path2key):
    print(getImages(city_name, path2key, 1, 'CityImg'))
    if getImages(city_name, path2key, 1, 'CityImg'):
        city_images = getImages(city_name, path2key, 1, 'CityImg')[0]
        # print(city_images)

        city_img = Image.open(f"./RSS/SRCH_IMGS/{city_images}").resize((200, 300))
        city_im = ImageTk.PhotoImage(city_img)

        fr.lb_pet_or_movie_image = Label(fr, image=city_im)
        lb_city_image.configure(image=city_im)
        lb_city_image.image = city_im
        lb_city_image.grid(row=0, column=0, pady=25)


    print(getImages(pet_or_movie_name, path2key, 1, 'PetOrMovieImg'))
    if getImages(pet_or_movie_name, path2key, 1, 'PetOrMovieImg'):
        pet_or_movie_images = getImages(pet_or_movie_name, path2key, 1, 'PetOrMovieImg')[0]
        # print(pet_or_movie_images)

        pet_or_movie_img = Image.open(f"./RSS/SRCH_IMGS/{pet_or_movie_images}").resize((200, 300))
        pet_or_movie_im = ImageTk.PhotoImage(pet_or_movie_img)

        fr.lb_pet_or_movie_image = Label(fr, image=pet_or_movie_im)
        lb_pet_or_movie_image.configure(image=pet_or_movie_im)
        lb_pet_or_movie_image.image = pet_or_movie_im
        lb_pet_or_movie_image.grid(row=0, column=2, pady=25)


def setText(fr, tb_magic_word, tb_city_name, tb_pet_or_movie_name, lb_city_image, lb_pet_or_movie_image, path2key):
    tb_magic_word.delete(1.0, 'end')
    city_name = tb_city_name.get('1.0', 'end - 1c')
    pet_or_movie_name = tb_pet_or_movie_name.get('1.0', 'end - 1c')
    tb_magic_word.insert(1.0, city_name + pet_or_movie_name)
    print("The Majestic Python is performing it's magic...")
    magic(fr, city_name, pet_or_movie_name, lb_city_image, lb_pet_or_movie_image, path2key)
    print('\nThe magical word is', city_name + pet_or_movie_name)

def clear(tb_city_name, tb_pet_or_movie_name, tb_magic_word):
    tb_magic_word.delete(1.0, 'end')
    tb_city_name.delete(1.0, 'end')
    tb_pet_or_movie_name.delete(1.0, 'end')

def restart(root):
    root.destroy()
    magicWordGenerator_GUI()

def magicWordGenerator_GUI():
    root = Tk()
    root.title('Magic Word Generator')
    root.geometry(f'800x600-{1900 - root.winfo_screenwidth()}-{1000 - root.winfo_screenheight()}')

    fr = Frame(root)

    lb_city_image = Label(fr)
    lb_city_image.image = None
    lb_pet_or_movie_image = Label(fr)
    lb_pet_or_movie_image.image = None

    lb_city_name = Label(fr, text='What is the name of the city where you grew up?')
    tb_city_name = Text(fr, width=30, height=1)

    lb_pet_or_movie_name = Label(fr, text='What is your pet or most favorite movie name?')
    tb_pet_or_movie_name = Text(fr, width=30, height=1)

    spells = ['Aa-braa-caa-daa-braa', 'Hocus-pocus', 'Alohomora', 'Expelliarmus', 'Patronus', 'Wingardium Levi-Osa', 'Accio', 'Alarte Ascendare', 'Aquamenti', 'Bombarda', 'Confringo', 'Everte Statum', 'Fianto Duri', 'Finite Incantatem', 'Immobulus', 'Periculum', 'Peskipiksi Pesternomi', 'Petrificus Totalus', 'Piertotum Locomotor', 'Protego Maxima', 'Reducto', 'Repello Inimicum', 'Repello Inimicum', 'Rictusempra', 'Riddikulus', 'Sectumsempra', 'Serpensortia', 'Stupefy', 'Tarantallegra', 'Vera Verto', 'Vipera Evanesca', 'Vulnera Sanentur']
    spell = choice(spells)


    btn = Button(fr, text=spell, command=lambda: setText(fr, tb_magic_word, tb_city_name, tb_pet_or_movie_name, lb_city_image, lb_pet_or_movie_image, path2key))

    lb_magic_word = Label(fr, text='The Magic Word is: ')
    tb_magic_word = Text(fr, width=30, height=1)

    control_panel = Label(fr, text='Control Panel:')

    clear_btn = Button(fr, text='CLEAR', command=lambda: clear(tb_city_name, tb_pet_or_movie_name, tb_magic_word))

    reset = Button(fr, text='RESTART', command=lambda: restart(root))

    Exit = Button(fr, text='EXIT', command=lambda: root.destroy)


    fr.place(anchor='center', relx=0.5, rely=0.5)

    lb_city_image.grid(row=0, column=0, pady=25)
    lb_pet_or_movie_image.grid(row=0, column=2, pady=25)

    lb_city_name.grid(row=1, column=0, pady=25)
    tb_city_name.grid(row=1, column=2, pady=25)

    lb_pet_or_movie_name.grid(row=2, column=0, pady=25)
    tb_pet_or_movie_name.grid(row=2, column=2, pady=25)

    btn.grid(row=3, column=1, pady=25)

    lb_magic_word.grid(row=4, column=0, pady=25)
    tb_magic_word.grid(row=4, column=2, pady=25)

    control_panel.grid(row=5, column=1, pady=35)

    clear_btn.grid(row=6, column=0, pady=25)
    reset.grid(row=6, column=1, pady=25)
    Exit.grid(row=6, column=2, pady=25)


    root.mainloop()

# magicWordGenerator_GUI()


