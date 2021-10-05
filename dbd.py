# https://dbd-api.herokuapp.com/
# https://dearvoodoo.github.io/DBD-API/

import requests
import json

url_killers = 'https://dbd-api.herokuapp.com/killers'
url_survivors = 'https://dbd-api.herokuapp.com/survivors'
url_perks = 'https://dbd-api.herokuapp.com/perks'

with open('killers.json', 'r') as f:
    data = json.loads(f.read())

class Killer:
    def get_killer(self, killer_id: int):
        with open('killers.json', 'r') as f:
            data = json.loads(f.read())
            self.name = data[killer_id]['name']
            self.full_name = data[killer_id]['full_name']
            self.power = data[killer_id]['power']
            self.weapon = data[killer_id]['weapon']
            self.speed = data[killer_id]['speed']
            self.terror_radius = data[killer_id]['terror_radius']
            self.overview = data[killer_id]['overview']
            self.wiki_url = data[killer_id]['wiki']
            self.portrait_url = data[killer_id]['icon']['portrait']
            perks = [perk for perk in data[killer_id]['perks']]
            self.perks = "\n".join(perks)

killer = Killer()

killer.get_killer(0)

print(killer.name)
print(killer.full_name)
print(killer.power)
print(killer.weapon)
print(killer.speed)
print(killer.overview)
print(killer.terror_radius)
print(killer.wiki_url)
print(killer.portrait_url)
print(killer.perks)