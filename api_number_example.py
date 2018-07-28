'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли
интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт,
и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа
во входном файле.
'''

import requests

with open ('dataset_24476_3.txt') as file:
    for line in file:
        number = line.strip()

        api_url = "http://numbersapi.com/"+number+'/math?json=true'

        res = requests.get(api_url)
        data = res.json()

        [print('Interesting') if data['found'] else print('Boring')]