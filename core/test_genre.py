from django.test import TestCase

# Create your tests here.
from core.genres import Genre, determine_genres


class TestGenre(TestCase):

    def test_determine_genre(self):
        rock = "Rock"
        self.assertTrue(Genre.ROCK in determine_genres(rock))

        rock = "Rock"
        self.assertTrue(Genre.ROCK in determine_genres(rock))

        heavy_rock = "Pop Rock"
        self.assertTrue(Genre.ROCK in determine_genres(heavy_rock))
        self.assertTrue(Genre.POP in determine_genres(heavy_rock))

        hiphop = "Hip-Hop"
        self.assertTrue((Genre.HIPHOP in determine_genres((hiphop))))
