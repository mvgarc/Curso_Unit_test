import requests

def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()