import json

data = {
    'nome': 'John Doe',
    'idade': 30,
    'é_estudante': False}

with open('data.json', 'w') as f:
    json.dump(data, f)