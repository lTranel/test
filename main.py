import requests
import folium
import logging


logging.basicConfig(filename='example.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


url = 'https://api.ipify.org/'

response = requests.get(url)
choice = int(input("1-узнать ip, 2-узнать инфу"))

if choice == 1:
    if response.status_code == 200:
        print('Ваш ip: ', response.text)
        logging.info(response.text)
    else:
        print('Ошибка при выполнении запроса')


def get_info_by_ip(ip='127.0.0.1'):
    #logging.basicConfig(filename='example.log', level=logging.INFO)
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[провайдер]': response.get('isp'),
            '[Организация]': response.get('org'),
            '[Страна]': response.get('country'),
            '[Регион]': response.get('regionName'),
            '[Город]': response.get('city'),
            '[Почтовый индекс]': response.get('zip'),
            '[Широта]': response.get('lat'),
            '[Долгота]': response.get('lon'),
        }
        logging.info(data)
        for a, b in data.items():
            print(f'{a} : {b}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('Ошибка при выполнении запроса')


def main():
    ip = input('Введите IP: ')

    get_info_by_ip(ip=ip)


if choice == 2:
    if __name__ == '__main__':
        main()
