import requests

class DadJoke:
    def get_dadjoke(self):
        headers = {'Accept': 'application/json'}
        r = requests.get('https://icanhazdadjoke.com/', headers=headers).json()
        self.joke = r['joke']