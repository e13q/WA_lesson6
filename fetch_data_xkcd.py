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
    response_dict = response.json()
    img_url = response_dict['img']
    comment = response_dict['alt']
    return img_url, comment
