import requests

day = input('Digite o dia: ')
month = input('Digite o mês: ')
year = input('Digite o ano: ')


response = requests.get(f'https://www.mercadobitcoin.net/api/BTC/day-summary/{year}/{month}/{day}/')


print(response.text)
