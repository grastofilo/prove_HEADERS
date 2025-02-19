import requests

# Creazione della sessione
session = requests.Session()

# Esegui una richiesta GET a httpbin.org per vedere quali header vengono inviati
response = session.get("https://httpbin.org/headers")
print("Header inviati (default):", response.json())
