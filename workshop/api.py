import requests

url = "https://official-joke-api.appspot.com/jokes/15"
dados = requests.get(url).json()

#Para buscar uma piada específica, basta alterar o número no final da URL. Por exemplo, para buscar a piada de número 15, a URL seria "https://official-joke-api.appspot.com/jokes/15".

print(dados["setup"])
print(dados["punchline"])