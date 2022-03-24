''' SUB-MODULE TO BE UTILIZED BY THE MAGIC WORD GENERATOR GUI PROGRAM FOR SEARCHING VARIOUS IMAGES '''


import requests as req
from random import shuffle
from PIL import Image
import urllib.request


def searchImages(query, key, count='inf'):
    res = req.get(f"https://serpapi.com/search.json?q={query}&tbm=isch&ijn=0&api_key={key}")
    if res.status_code == 200:
        print('Success! Images Found!\nStatus Code =', res.status_code)
    else:
        print('Oops! Images not Found!\nStatus Code =', res.status_code)
    # data = res.text
    res_json = res.json()

    print('\033[4mImage Search Results\033[0m...')

    print(res_json)

    res_images = []

    for i in res_json.items():
        for j in range(len(i)):
            if i[j] == 'images_results':
                for k in i[j + 1]:
                    res_images.append(k['thumbnail'])

    shuffle(res_images)

    return res_images if count == 'inf' else res_images[:count]

def search(query, path2key, count):
    f = open(path2key, 'r')
    key = f.read()
    f.close()
    searches = searchImages(query, key, count)
    print(searches)
    return searches

def getImages(query, path2key, count, img_name):
    res_images = search(query, path2key, count)
    images_names = []
    for i in range(len(res_images)):
        # urllib.request.urlretrieve(searches[i], f"Img{i + 1}.png")
        # searches = search(query, path2key)
        urllib.request.urlretrieve(res_images[i], f"./RSS/SRCH_IMGS/{img_name}{i + 1}.png")
        # img = Image.open(f"Img{i + 1}.png")
        img = Image.open(f"./RSS/SRCH_IMGS/{img_name}{i + 1}.png")
        images_names.append(f"{img_name}{i + 1}.png")
        # img.show()
    return images_names

# print(getImages('Meghalaya', "./RSS/PVT_RS/pvt.txt", 2, 'Img'))


