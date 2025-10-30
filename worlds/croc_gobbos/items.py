from typing import NamedTuple

from BaseClasses import Item, ItemClassification

class CrocItem(Item):
    game: str = "Croc: The Legend of the Gobbos"

class CrocItemData(NamedTuple):
    id: int | None = None
    type: ItemClassification = ItemClassification.filler
    category: str | None = None
    qty: int = 1