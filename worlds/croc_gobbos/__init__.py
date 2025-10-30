from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld

from .options import CrocOptions

class CrocWebWorld(WebWorld):
    theme = "jungle"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to setting up and playing the Croc randomizer.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["RoobyRoo"]
    )

    tutorials = [setup_en]

class CrocWorld(World):
    """The Archipelago Randomizer World for Croc: The Legend of the Gobbos. If you see this on a website, I didn't finish the documentation, so yell at me for it."""

    game = "Croc: The Legend of the Gobbos"
    options: CrocOptions
    options_dataclass = CrocOptions
    web = CrocWebWorld()
