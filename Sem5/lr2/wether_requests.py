'''
Task 2. https://repl.it/@zhukov/WindingRoughApi#main2.py
'''

import requests as req

def get_wether(city, APIkey):
    r = req.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={APIkey}').json()
    if int(r["cod"]) == 200:
        name = r["name"]
        country = r["sys"]["country"]
        coord = r["coord"]["lon"], r["coord"]["lat"]
        time = int(r["timezone"]) / 3600
        if time > 0:
            timezone = f'UTC+{time}'
        else:
            timezone = f'UTC{time}'
        temp = r["main"]["feels_like"]

        result = {
            'name': f'{name}',
            'country': f'{country}',
            'coord': {
                'lon': f'{coord[0]}',
                'lat': f'{coord[1]}'
            },
            'timezone': f'{timezone}',
            'temp': f'{temp}'
        }
    else:
        result = f'Error: {r["message"]}, {r["cod"]}'
    return result

if __name__ == '__main__':
    cities = ['Chicago, US', 'Moscow, RU', 'Saint Petersburg, RU', 'Dhaka, BD']
    APIkey = 'bf3e830b2046f4f7ef63ff2ca100c632'
    res = []
    for city in cities:
        res += [get_wether(city, APIkey)]
    
    # Chicago
    assert res[0]['coord'] == {'lon': '-87.65', 'lat': '41.85'}, ""
    assert res[0]['timezone'] == 'UTC-5.0', ""

    # Moscow
    assert res[1]['coord'] == {'lon': '37.62', 'lat': '55.75'}, ""
    assert res[1]['timezone'] == 'UTC+3.0', ""

    # Saint Petersburg
    assert res[2]['coord'] == {'lon': '30.26', 'lat': '59.89'}, ""
    assert res[2]['timezone'] == 'UTC+3.0', ""

    # Dhaka
    assert res[3]['coord'] == {'lon': '90.41', 'lat': '23.71'}, ""
    assert res[3]['timezone'] == 'UTC+6.0', ""

    for el in res:
        print(el)