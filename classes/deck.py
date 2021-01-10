import random
from classes.card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:

	def __init__(self):
		self.all_cards = []
		for suit in suits:
			for rank in ranks:
				self.all_cards.append(Card(suit,rank))

	def shuffle(self):
		random.shuffle(self.all_cards)

	def deal_one(self):
		if len(self.all_cards) > 0:
			return self.all_cards.pop()
		else:
			print("There is no more Cards to deal. Game ended")
		