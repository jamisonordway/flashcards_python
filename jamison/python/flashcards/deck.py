class Deck:

  def __init__(self, cards):
    self.cards = cards

  def count(self):
    return len(self.cards)
  
  def cards_in_category(self, category):
    included = []
    for card in self.cards:
      if card.category == category:
        included.append(card)
    return included