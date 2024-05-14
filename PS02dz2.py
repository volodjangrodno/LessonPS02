import requests

# URL API
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса
params = {
    "userId": 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверка статуса ответа
if response.status_code == 200:
    # Преобразование ответа в формат JSON
    data = response.json()

    # Печать полученных записей
    for record in data:
        print(record)
else:
    print(f"Не удалось получить данные. Статус код: {response.status_code}")