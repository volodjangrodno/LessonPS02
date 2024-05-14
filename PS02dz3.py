import requests

# URL API для отправки POST-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Печать статус-кода ответа
print(f"Статус-код: {response.status_code}")

# Печать содержимого ответа
print("Содержимое ответа:")
print(response.json())