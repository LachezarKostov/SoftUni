from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if card.name in [c.name for c in self.cards]:
            raise ValueError(f"Card {card.name} already exists!")
        else:
            self.cards.append(card)
            self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Player cannot be an empty string!")
        list_of_cards_names = [c.name for c in self.cards]
        index = list_of_cards_names.index(card)
        self.cards.pop(index)
        self.count -= 1

    def find(self, name: str):
        list_of_cards_names = [c.name for c in self.cards]
        index = list_of_cards_names.index(name)
        return self.cards[index]