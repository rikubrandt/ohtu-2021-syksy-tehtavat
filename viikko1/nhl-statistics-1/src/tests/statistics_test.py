import statistics
import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search(self):
        self.player = self.statistics.search("Semenko")
        self.assertEqual(self.player.name, "Semenko")

    def test_team_players(self):
        list = self.statistics.team("EDM")
        self.assertGreater(len(list), 2)

    def test_top_scorer(self):
        self.assertEqual(self.statistics.top_scorers(1)[0].name, "Gretzky")
    
    def test_player_not_found(self):
        self.assertEqual(None, self.statistics.search("asdasdasda"))