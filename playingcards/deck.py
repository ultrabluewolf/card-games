import random, playingcards
from playingcards.card import *

class Deck:
	"""Deck of playing cards"""
	def __init__(self):
		self.stack = []
	
	#TODO: create fresh default deck
	def gen(self):
		self.stack = []
		for suit_i in range(Card.SUITS):
			for rank_i in range(Card.RANKS):
				self.stack.append(Card(rank_i,suit_i))
		return self
			
	
	def append(self,card):
		self.stack.append(card)
	def pop(self):
		return self.stack.pop()
	
	def shuffle(self):
		random.seed()
		random.shuffle(self.stack)
		return self
	
	def __len__(self):
		return len(self.stack)
	
	def __str__(self):
		str = ''
		for card in self.stack:
			str += card.__str__() + '|'
		return str
