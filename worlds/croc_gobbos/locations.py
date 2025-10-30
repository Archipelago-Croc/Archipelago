from typing import NamedTuple
from collections.abc import Callable

from BaseClasses import Location, CollectionState

class CrocLocation(Location):
    game = "Croc: Legend of the Gobbos"

class CrocLocationData(NamedTuple):
    region: str
    id: int | None = None
    rule: Callable[[CollectionState, int], bool] = lambda state, player: True
