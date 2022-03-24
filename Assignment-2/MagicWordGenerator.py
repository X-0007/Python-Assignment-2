''' MODULE FOR THE MAGIC WORD GENERATOR CLI PROGRAM '''


def magicWordGenerator():
    print('What is the name of the city where you grew up?')
    city_name = input()
    print('What is your pet or most favourite movie name?')
    pet_or_movie_name = input()
    print('The magical word is', city_name + pet_or_movie_name)


