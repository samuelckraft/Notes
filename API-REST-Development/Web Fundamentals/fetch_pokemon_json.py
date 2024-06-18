import requests
import json

#Fetching data from the pokemon ai
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

json_data = response.text



#Converting JSON to python object (dictionary)

pikachu_data = json.loads(json_data)

#Accessing data
print(pikachu_data["name"]) #output: pikachu
print(pikachu_data['types']) #output: {'slot': 1, 'type': {'name': 'electric', 'url': 'https://pokeapi.co/api/v2/type/13/'}}