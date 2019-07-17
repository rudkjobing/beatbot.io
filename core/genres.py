from enum import Enum
from typing import Optional, List


class Genre(Enum):
    ROCK = "Rock"
    POP = "Pop"
    METAL = "Metal"
    JAZZ = "Jazz"
    PUNK = "Punk"
    HIPHOP = "HipHop"
    WORLD = "World"
    FOLK = "Folk"
    SYNTH = "Synth"


def determine_genre(raw: str) -> List[Genre]:
    resulting_genres = []
    normalized_raw: str = raw.lower()
    for genre in Genre:
        normalized_genre: str = genre.value.lower()
        if normalized_genre in normalized_raw:
            resulting_genres.append(genre)
    return resulting_genres
