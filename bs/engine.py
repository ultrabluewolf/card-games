
import playingcards
from playingcards.deck import *
from playingcards.hand import *
from playingcards.card import *

class Engine:
	"""Game Engine"""
	def __init__(self, num_players):
		#distribute deck among hands
		self.decks = [Deck().gen().shuffle()]
		self.players = []
		for i in range(num_players):
			self.players.append(Hand())
		#print len(self.players)
		player_idx=0
		while len(self.decks[0]):
			card = self.decks[0].pop()
			self.players[player_idx].add(card)
			if player_idx < num_players-1:
				player_idx+=1
			else:
				player_idx=0
		#print self.decks[0]
		for hand in self.players:
			print hand
			
		
		#self.hands = []
		#self.mappings = {}
		
		"""deck = Deck()
		for i in range(10):
			deck.append(Card(i,i%4))
		
		deck.gen()
		print 'size: ' + str(len(deck))
		print deck
		
		hand = Hand()
		hand.add(Card(3,Card.CLBS))
		hand.add(Card(Card.KNG,Card.SPDS))
		hand.add(Card(3,Card.CLBS))
		hand.remove(Card(3,Card.CLBS))
		hand.remove(Card(3,Card.CLBS))
		hand.remove(Card(Card.KNG,Card.SPDS))
		print hand
		"""
	
