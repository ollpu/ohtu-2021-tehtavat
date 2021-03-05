import requests
from datetime import datetime
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []
    wanted_nationality = "FIN"

    for player_dict in response:
        if player_dict['nationality'] == wanted_nationality:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
            )

            players.append(player)
    players.sort(reverse=True, key=lambda p: p.score)

    print(f"Players from {wanted_nationality} {datetime.now()}\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
