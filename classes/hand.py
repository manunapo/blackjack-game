from classes.card import Card

class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.has_ace = False
		
	def get_hand_value(self):
		return self.value

	def add_card(self,card):
		if card.rank == 'Ace':
			self.has_ace = True
		if ((self.value + card.value) > 21) and (self.has_ace):
			self.value += card.value
			self.value -= 10
		else:
			self.value += card.value
		self.cards.append(card)

