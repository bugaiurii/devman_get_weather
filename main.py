import requests

city = 'city'

while city != 'end':
    city = input('Укажите название города: ')

    url_template = 'http://wttr.in/{name}?MTnq&lang=ru'
    url = url_template.format(name=city)

    response = requests.get(url)

    print(response.text)
    print('Для выхода из программы, введите: end.')





