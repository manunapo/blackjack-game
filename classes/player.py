from classes.card import Card
from classes.hand import Hand

class Player:

	def __init__(self,name,total_money):
		self.name = name
		self.hand = Hand()
		self.total_money = total_money
		self.bet = 0

	def add_card(self,new_card):
		self.hand.add_card(new_card)

	def __str__(self):
		return f'Player {self.name} has {len(self.all_cards)} cards'

	#Will bet 'amout' or total_money
	#If total_money = 0, cant bet -> game ends
	def do_bet(self,amount):
		if self.total_money < 1:
			print('Not enough money to bet. Ending the game')
			return 0
		if self.total_money >= amount:
			self.total_money -= amount
			print(f'{self.name} is betting {amount}')
			self.bet = amount
		else:
			print(f'{self.name} is betting {self.total_money}')
			self.bet = self.total_money
			self.total_money = 0
		return self.bet

	def hand_value(self):
		return self.hand.get_hand_value()

	def lose_bet(self):
		tmp = self.bet
		self.bet = 0
		return tmp

	def win_bet(self):
		self.total_money += self.bet * 2
		tmp = self.bet * 2
		self.bet = 0
		return tmp

	def reset(self):
		self.hand = Hand()
		self.bet = 0

	def tie(self):
		self.total_money += self.bet