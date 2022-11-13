import requests


payload = {'MTnq': '', 'lang': 'ru'}

def city1():

    city = 'svo'

    url_template = 'http://wttr.in/{name}'
    url = url_template.format(name=city)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    print(response.text)



def city2():
    city = 'London'

    url_template = 'http://wttr.in/{name}'
    url = url_template.format(name=city)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    print(response.text)

def city3():
    city = 'Череповец'

    url_template = 'http://wttr.in/{name}'
    url = url_template.format(name=city)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    print(response.text)


def main():
    city1()
    city2()
    city3()

if __name__ == '__main__':
    main()