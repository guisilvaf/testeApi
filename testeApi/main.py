# import requests
import csv
import json


# api = requests.get("")  #Request para api da loja

def csv_convert(csv_path, json_path):  # Função para converter CSV para JSON
    jsonData = {}  # dictionary

    with open(csv_path, encoding='utf-8') as csvfile:
        csvData = csv.DictReader(csvfile)

        for rows in csvData:  # Converter cada coluna do dictionary
            key = rows.get("Codigo interno")
            jsonData[key] = rows

    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(jsonData, indent=5))


# Chamando os arquivos de cada extensão
csv_path = r'items.csv'
json_path = r'itemList.json'

csv_convert(csv_path, json_path)  # Chamando a função
