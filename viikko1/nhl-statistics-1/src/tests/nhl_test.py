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

class TestNHL(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics(PlayerReaderStub())
    
    def test_etsi_pelaaja_joka_loytyy(self):
        self.assertEqual(self.stats.search('Semenko').name, 'Semenko')
    
    def test_etsi_pelaaja_joka_ei_loydy(self):
        self.assertEqual(self.stats.search('Harjula'), None)
    
    def test_oikeat_pelaajat_joukkueesta(self):
        oikeat = ['Semenko', 'Kurri', 'Gretzky']
        vastaukset = self.stats.team('EDM')
        vastaukset = [vastaus.name for vastaus in vastaukset]
        self.assertEqual(vastaukset, oikeat)
    
    def test_oikeat_eniten_maaleja_tehneet(self):
        oikeat = ['Gretzky', 'Lemieux', 'Yzerman']
        vastaukset = self.stats.top_scorers(2)
        vastaukset = [vastaus.name for vastaus in vastaukset]
        self.assertEqual(vastaukset, oikeat)
