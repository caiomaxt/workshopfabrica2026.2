import requests

url = "https://official-joke-api.appspot.com/jokes/random"
response = requests.get(url).json()

print(response["setup"])
print(response["punchline"])