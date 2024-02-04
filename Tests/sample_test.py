"""
Script to make tests
"""


import unittest
from scripts.Filtering import NBADataFilter
import pandas as pd

class TestNBADatasetFilter(unittest.TestCase):
 

    def test_filter_by_points_exact(self):
        """Prueba filtrar exactamente 20 puntos."""
        result = self.nba_filter.filter_by_points(20)
        self.assertEqual(len(result))

    def test_filter_by_points_above(self):
        """Prueba filtrar más de 20 puntos."""
        result = self.nba_filter.filter_by_points(15)
        self.assertEqual(len(result))

    def test_filter_by_height_below(self):
        """Prueba filtrar por altura debajo de 190 cm."""
        result = self.nba_filter.filter_by_height(180)
        self.assertEqual(len(result))

    def test_filter_by_height_above(self):
        """Prueba filtrar por altura encima de 200 cm."""
        result = self.nba_filter.filter_by_height(200)
        self.assertEqual(len(result))

    def test_filter_by_team_multiple(self):
        """Prueba filtrar por equipo con múltiples coincidencias."""
        result = self.nba_filter.filter_by_team('LAL')
        self.assertEqual(len(result))

    def test_filter_by_team_single(self):
        """Prueba filtrar por equipo con una sola coincidencia."""
        result = self.nba_filter.filter_by_team('NYK')
        self.assertEqual(len(result))

    def test_filter_by_country_usa(self):
        """Prueba filtrar por país 'USA'."""
        result = self.nba_filter.filter_by_country('USA')
        self.assertEqual(len(result))

    def test_filter_by_country_no_match(self):
        """Prueba filtrar por país sin coincidencias."""
        result = self.nba_filter.filter_by_country('Italy')
        self.assertEqual(len(result))

    def test_filter_by_assists_range_low(self):
        """Prueba filtrar por asistencias en el rango bajo."""
        result = self.nba_filter.filter_by_assists(3)
        self.assertEqual(len(result))

    def test_filter_by_assists_range_high(self):
        """Prueba filtrar por asistencias en el rango alto."""
        result = self.nba_filter.filter_by_assists(8)
        self.assertEqual(len(result))

    # Agregar más pruebas para llegar a 15
    def test_filter_no_players_above_50_points(self):
        """Asegurar que no hay jugadores con más de 50 puntos."""
        result = self.nba_filter.filter_by_points(50)
        self.assertEqual(len(result))

    def test_filter_by_age_young_players(self):
        """Prueba filtrar jugadores jóvenes (menores de 25)."""
        result = self.nba_filter.filter_by_age(0, 25)
        self.assertEqual(len(result))

if __name__ == "__main__":
    main()
