import requests
from config import API_URL, API_KEY


class APIClient:
    def __init__(self):
        self.base_url = API_URL
        self.headers = {
            "apikey": f"{API_KEY}",
            "Content-Type": "application/json"
        }

    def chamar_endpoint(self, endpoint, urls_params=None):
        endpoint = endpoint.format(**urls_params)
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
