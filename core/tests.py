from django.test import TestCase

# Create your tests here.
from core.genres import Genre, determine_genre


class TestGenre(TestCase):

    def test_determine_genre(self):
        rock = "Rock"
        self.assertTrue(Genre.ROCK in determine_genre(rock))

        heavy_rock = "Pop Rock"
        self.assertTrue(Genre.ROCK in determine_genre(heavy_rock))
        self.assertTrue(Genre.POP in determine_genre(heavy_rock))
