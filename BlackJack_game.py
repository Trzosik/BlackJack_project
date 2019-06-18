class Card:

    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
    suits = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand:

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for 