import unittest
from statistics import Statistics
from player import Player

PLAYERS = [
    Player("Semenko", "EDM", 4, 12), # score 18
    Player("Lemieux", "PIT", 45, 54),# 99
    Player("Kurri",   "EDM", 37, 53),# 90
    Player("Yzerman", "DET", 42, 56),# 98
    Player("Gretzky", "EDM", 35, 89) # 124
]
class PlayerReaderStub:
    def get_players(self):
        return PLAYERS

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_present(self):
       player = self.statistics.search("Yzerman")
       # No custom comparison operator, so this assumes Statistics
       # does not clone Players.
       self.assertEqual(player, PLAYERS[3])

    def test_search_not_present(self):
        player = self.statistics.search("Laine")
        self.assertEqual(player, None)

    def test_team(self):
        team = self.statistics.team("EDM")
        self.assertEqual(team, [PLAYERS[0], PLAYERS[2], PLAYERS[4]])

    def test_top_scorers(self):
        players = self.statistics.top_scorers(2)
        self.assertEqual(players, [PLAYERS[4], PLAYERS[1]])
