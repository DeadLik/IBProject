import requests

API = 'API_KEY'

while True:
    print('1. Информация по ip\n'
          '2. Комментарии по ip\n'
          '3. Выход')
    menu = int(input('Выберите запрос: '))

    if menu == 1:
        ip = input('Введите IP адрес, например "8.8.8.8": ')

        url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip}'

        headers = {
            "accept": "application/json",
            "x-apikey": API
        }

        response = requests.get(url, headers=headers)
        text = response.text

        with open('Result/result_ip.json', 'w+', encoding='utf-8') as f:
            f.write(text)
        print('Данные записаны')

    elif menu == 2:
        ip = input('Введите IP адрес, например "8.8.8.8": ')

        url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip}/comments?limit=10'

        headers = {
            "accept": "application/json",
            "x-apikey": API
        }

        response = requests.get(url, headers=headers)
        text = response.text

        with open('Result/result_comment_ip.json', 'w+', encoding='utf-8') as f:
            f.write(text)
        print('Данные записаны')

    elif menu == 3:
        break
