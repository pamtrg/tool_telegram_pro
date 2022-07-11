import requests

class Connect_API:
    def __init__(self) -> None:
        pass
    def _Connect(self):
        import requests

requests.get("https://proxy.webshare.io/api/profile/", headers={"Authorization": "Token APIKEY"})