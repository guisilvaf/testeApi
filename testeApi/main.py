import requests
import json
import datetime


# api = requests.get("Zj7P7qnkl-D9fRIpMyjFB5iLaK0qVYFTiYEHk1Vj4j8")  #Request para pegar a api da loja.

data = open("items.csv", 'r', encoding='utf-8').readlines() #Abrindo planilha.
dictionary = dict.fromkeys(data) #Transformando a planilha em um dictionary

#Abrindo a planilha como .JSON.
with open(r'data.json', 'w', encoding='utf-8') as file:
    json.dump(dictionary, file, indent=2)

def floatPrice():
    for price in dictionary['item']:
        round(['Preco_regular'], 2) #Arredondando o preço para 2 casas decimais
        float(['Preco_regular']) #Transformando o preço em float


'''requests.put("Zj7P7qnkl-D9fRIpMyjFB5iLaK0qVYFTiYEHk1Vj4j8", dictionary={'internal_code':'Codigo', 'name':'Nome', 'price':'Preco_regular', 'visible':'Ativo',
 'stock':'Estoque', 'barcodes':'Codigo_barras', 'promo_price':'Promocao', 'promo_end_at':'Termino_promocao'}) #Request para enviar informações para a API. '''