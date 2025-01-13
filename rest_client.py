import requests

# Llamar al método 'add'
response_add = requests.post('http://127.0.0.1:8000/add', json={'a': 5, 'b': 3})
print(f'5 + 3 = {response_add.json()["result"]}')

# Llamar al método 'subtract'
response_subtract = requests.post('http://127.0.0.1:8000/subtract', json={'a': 5, 'b': 3})
print(f'5 - 3 = {response_subtract.json()["result"]}')