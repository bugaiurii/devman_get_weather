import requests

city = 'city'
payload = {'MTnq': '', 'lang': 'ru'}

while True:

    city = input('Укажите название города: ')
    if city == 'end':
        break
    else:

        try:

            url_template = 'http://wttr.in/{name}'
            url = url_template.format(name=city)

            response = requests.get(url, params=payload)
            response.raise_for_status()

            print(response.text)

        except:
            print(None)
    print('Для выхода из программы, введите: end.')
