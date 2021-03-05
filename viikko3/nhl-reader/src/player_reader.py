import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        return [
            Player(
                name=player_dict['name'],
                nationality=player_dict['nationality'],
                team=player_dict['team'],
                goals=player_dict['goals'],
                assists=player_dict['assists'],
            )
            for player_dict in response
        ]
