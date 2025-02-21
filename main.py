import requests
from io import BytesIO
from PIL import Image
import random
import time
import pygame

GEOCODER_API = "8013b162-6b42-4997-9691-77b7074026e0"
YANDEX_MAPS_API = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

towns_list = ['Киров', 'Москва', 'Цюрих', 'Шадринск', 'Лондон', 'Верне', 'Мараба', 'Росарио', 'Новый Орлеан', 'Кумаси']
ZOOM = "16"
SLIDE_DURATION = 2
WINDOW_SIZE = (450, 450)



def show_pic_cords(cor1, cor2):
    if cor1 is None or cor2 is None:
        return None

    ll = '{},{}'.format(cor1, cor2)

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {
            "ll": ll,
            "size": "450,450",
            "l": "map",
            "z": ZOOM,
            "apikey": YANDEX_MAPS_API
        }

    response = requests.get(map_api_server, params=map_params)
    if response.status_code != 200:
        print(f"err while loading map of {response.status_code}: {response.text}")
        return

    img = Image.open(BytesIO(response.content))
    if is_city_area(img):
        return BytesIO(response.content)
