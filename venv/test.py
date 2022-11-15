import requests


payload = {'MTnq': '', 'lang': 'ru'}

def get_weather(city):

    #city = 'svo'

    url_template = 'http://wttr.in/{name}'
    url = url_template.format(name=city)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    print(response.text)


def main():
    get_weather('svo')
    get_weather('london')
    get_weather('Череповец')

if __name__ == '__main__':
    main()