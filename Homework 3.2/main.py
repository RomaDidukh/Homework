import requests

# Відправляємо GET-запит до Google
response = requests.get('https://www.google.com')

# Виводимо отриманий HTML-код в терміналі
print(response.text)
 