import requests
import random

class ShortLinkClient:
    def __init__(self, token, base_url="https://api.shrt.tsell.cc"):
        self.base_url = base_url
        self.token = token

    def create_link(self, redirect_url, code=None, expired_at=None):

        if not code:
            alphabet = 'xbcdefghiuklmnopqrstuvwxyz0123456789'
            code = ''.join(random.choices(alphabet, k=6))

        payload = {
            "redirect_url": redirect_url,
            "code": code,
            "expired_at": expired_at,
        }

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        response = requests.post(f"{self.base_url}/v1/backend/link", json=payload, headers=headers)
        response.raise_for_status()

        resp_data = response.json()

        return resp_data['Url']