from config_token import WETHER_TOKEN
import requests
from pprint import pprint
import datetime
def open_wether(city, WETHER_TOKEN):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WETHER_TOKEN}&units=metric'
        )
        print(r)
        data = r.json()
        # pprint(data)

        city = data['name']
        cur_wether = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(f"Погода в городе: {city}\nТемпература: {cur_wether}C\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}\n"
              f"Восход солнца: {sunrise_timestamp}")


    except Exception as ex:
        print(ex)
        print("нет такого города")

def main():
    city = input("Введите город: ")
    open_wether(city, WETHER_TOKEN)

if __name__ == '__main__':
    main()
