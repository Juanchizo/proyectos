import requests

url = "https://postman-echo.com/post"
data = {"mensaje": "hola"}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Respuesta:", response.json())