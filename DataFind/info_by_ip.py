import requests


def get_data(ip_addr: str) -> None:
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip_addr}').json()
        print(response)
    except requests.exceptions.ConnectionError:
        print('Connection error occured!')


get_data('222.18.154.102')


