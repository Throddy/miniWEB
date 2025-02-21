from io import BytesIO
import requests
from PIL import Image



def ll_cords(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        pass
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    return toponym_coodrinates.split(" ")[::-1]


def show_find(adress='', cords1='', cords2=''):
    if adress:
        ll = ll_cords(adress)
        print(ll)
    if cords1 and cords2:
        ll = (str(cords1), str(cords2))
        print(ll)
    delta = "0.005"
    apikey = "46f543e5-8557-4b4f-92bc-8fbd63dcd53d"
    org_point = f'{ll[1]},{ll[0]}'

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([ll[1], ll[0]]),
        "spn": ",".join([delta, delta]),
        "apikey": apikey,
        'pt': f'{org_point},pm2dgl'
    }
    print(map_params)
    map_api_server = "https://static-maps.yandex.ru/v1"
    response = requests.get(map_api_server, params=map_params)
    print(response)
    im = BytesIO(response.content)
    opened_image = Image.open(im)
    opened_image.save('pick_me.png')


show_find(adress="Калининград")
