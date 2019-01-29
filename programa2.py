#print (lista)

#numero = indice do dicionário
#quantidade = contador de repetições

#dicionario = {numero:quantidade}

#transformar a lista em conjunto
#contar quantas vezes cada elemento do conjunto aparece na lista



import requests
import json

lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)


conjunto = set(lista)
dicionario = {}
quantidade = 0
contador = 0

for numero in conjunto:
   
   if numero == lista [contador]:
      quantidade += 1
      contador +=1
   else:
      contador +=1
   dicionario[numero]=quantidade
   #quantidade = 0
   contador = 0

print (dicionario)

