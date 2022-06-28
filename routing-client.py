import requests

URL = "http://localhost:8080/calculateSS"

street = "123 Main"
driver = "Gumby"

PARAMS = {
    'street' :street,
    'driver': driver
}

r = requests.get(url = URL, params = PARAMS)
data = r.json()

print(data)

