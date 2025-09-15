import time

import httpx

# Инициализируем клиент
'''
 client = httpx.Client() - создаёт экземпляр клиента httpx.Client, который позволяет управлять HTTP-соединениями и 
 повторно использовать TCP-соединение между запросами.
'''
# Инициализируем клиент с авторизацией
client = httpx.Client(
    base_url="http://localhost:8003",
    timeout=100,
    headers={"Authorization": "Bearer ..."}
)

payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем POST-запрос, используя клиент
response = client.post("/api/v1/users", json=payload)

# Выводим ответ в консоль
print(response.text)


