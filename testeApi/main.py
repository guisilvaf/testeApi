import requests
import json


# api = requests.get("")  #Request para pegar a api da loja

data = open("items.csv", 'r', encoding='utf-8').readlines()
dictionary = dict.fromkeys(data)

with open(r'data.json', 'w', encoding='utf-8') as file:
    json.dump(dictionary, file, indent=2)


#print(data)
print(type(dictionary))

# requests.post("", data={}) #Request para enviar informações para a API