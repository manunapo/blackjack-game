from classes.player import Player
from classes.deck import Deck
from classes.hand import Hand

player_name = input("Hello, who is going to play?")
the_player_one = Player(player_name,200)
the_dealer = Player("Dealer",5000)
the_deck = Deck()
print("Starting the game...")
game_on = True
playing = True

def take_bet(player):
	while True:
		try:
			new_bet = int(input(f"Please {player.name} make your bet: "))
		except:
			print("Bet should be numeric")
		break

	real_bet = player.do_bet(new_bet)
	the_dealer.do_bet(real_bet)
	return real_bet > 0

def give_cards():
	the_deck.shuffle()
	the_player_one.add_card(the_deck.deal_one())
	the_player_one.add_card(the_deck.deal_one())
	the_dealer.add_card(the_deck.deal_one())
	the_dealer.add_card(the_deck.deal_one())


def show_cards(player,hide_dealer_card):
	index = 0
	print("-----------")
	if not hide_dealer_card:
		print(f"{player.name} ({player.total_money}) score is {player.hand_value()} with cards:")		
	else:
		print(f"{player.name} ({the_dealer.total_money}) cards:")
	for card in player.hand.cards:
		if hide_dealer_card and index == 1:
			print("**hide**")
		else:
			print(card)
		index += 1
	print(f"-----------")

def hit_or_stand(player):
	while True and player.hand_value() < 21:
		hit = input("Do you want one more card? Y/N").lower()
		if hit == "y":
			player.add_card(the_deck.deal_one())			
		else:
			print(f'The {player.name} ({player.total_money}) stands with {player.hand_value()}')
			break
		show_cards(player,False)

def player_wins(player):
    the_bet = player.bet
    the_dealer.lose_bet()
    player.win_bet()
    print(f'The {player.name} ({player.total_money}) wins {the_bet}! Now he has {player.total_money}')
    print(f'The {the_dealer.name} ({player.total_money}) losts {the_bet}! Now he has {the_dealer.total_money}')

def dealer_wins(player):
    the_bet = player.bet
    the_dealer.win_bet()
    player.lose_bet()
    print(f'The {the_dealer.name} ({the_dealer.total_money}) wins {the_bet}! Now he has {the_dealer.total_money}')
    print(f'The {player.name} ({player.total_money}) losts {the_bet}! Now he has {player.total_money}')

def tie(player):
	player.tie()
	the_dealer.tie()

while game_on:

	if not take_bet(the_player_one):
		playing = False
		game_on = False
		break
	give_cards()
	show_cards(the_player_one,False)
	show_cards(the_dealer,True)

	while playing:
		hit_or_stand(the_player_one)
		if the_player_one.hand_value() > 21:
			dealer_wins(the_player_one)
			break
		else:
			show_cards(the_dealer,False)
			while the_dealer.hand_value() < 17:
				the_dealer.add_card(the_deck.deal_one())
				show_cards(the_dealer,False)
			if the_dealer.hand_value() > 21:
				player_wins(the_player_one)
				break
		playing = False

		if the_player_one.hand_value() > the_dealer.hand_value():
			player_wins(the_player_one)
		elif the_player_one.hand_value() < the_dealer.hand_value():
			dealer_wins(the_player_one)
		else:
			tie(the_player_one)
			print("Has a TIE!")
	
	answer = input("Do you want to play another hand? Y/N").upper()
	while answer != "Y" and answer != "N":
		answer = input("Do you want to play another hand? Y/N")
	if answer == "N":
		print("Game finished")
		game_on = False
	playing = True
	the_player_one.reset()
	the_dealer.reset()