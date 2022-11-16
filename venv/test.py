import requests


payload = {'MTnq': '', 'lang': 'ru'}

def get_weather(city):


    url_template = 'http://wttr.in/{name}'
    url = url_template.format(name=city)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    print(response.text)


def main():
    cities = ['svo', 'London', 'Череповец']
    for city in cities:
        get_weather(city)


if __name__ == '__main__':
    main()