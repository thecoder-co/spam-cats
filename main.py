import requests
import random
import json
#from alright import WhatsApp

char = ('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')


def random_name():
    name = ''
    for i in range(8):
        name += random.choice(char)
    return name


def get_image():
    data = requests.get('https://meme-api.herokuapp.com/gimme/Cats')
    return json.loads(data.text)['url']


def download_images(number):
    #messenger = WhatsApp()
    for i in range(number):
        image_url = get_image()
        img_data = requests.get(image_url).content
        name = f'{random_name()}.{image_url.split(".")[-1]}'

        with open(name, 'wb') as handler:
            handler.write(img_data)
        """ messenger.find_user('2349072227693')
        messenger.send_image(name) """


download_images(1)
