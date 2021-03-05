from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        wanted_players = filter(lambda p: p.nationality == nationality, self.players)
        return sorted(wanted_players, reverse=True, key=lambda p: p.score)
