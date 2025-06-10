
from dataclasses import dataclass
print("decks/deck: Materializing a Card type.")
@dataclass
class Card:
    front: str
    back : str

print("decks/deck: Initializing the Deck Application.")
# This deck represents your application.
global deck
deck = []
