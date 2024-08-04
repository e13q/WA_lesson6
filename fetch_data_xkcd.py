import requests


def get_comix_count():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    comix_count = response.json().get('num')
    return comix_count


def fetch_comix(index):
    url = f'https://xkcd.com/{index}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    img_url = response['img']
    comment = response['alt']
    return img_url, comment
