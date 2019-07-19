from enum import Enum
from typing import Optional, List, Set


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
    URBAN = "Urban"


def determine_genres(raw: str) -> Set[Genre]:
    resulting_genres = set()
    normalized_raw: str = raw.lower().replace("-", "").replace(" ", "").replace("heavy", "metal")
    for genre in Genre:
        normalized_genre: str = genre.value.lower()
        if normalized_genre in normalized_raw:
            resulting_genres.add(genre)
    return resulting_genres
