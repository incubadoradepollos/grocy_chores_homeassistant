import requests
from homeassistant.helpers.entity import Entity

API_URL = "https://api.tu-dominio.com/items"

def setup_platform(hass, config, add_entities, discovery_info=None):
    response = requests.get(API_URL)
    data = response.json()
    items = data.get("items", [])
    sensors = [APISensor(item) for item in items]
    add_entities(sensors)

class APISensor(Entity):
    def __init__(self, item):
        self._name = item["name"]
        self._state = item["state"]

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        response = requests.get(API_URL)
        data = response.json()
        for item in data.get("items", []):
            if item["name"] == self._name:
                self._state = item["state"]
