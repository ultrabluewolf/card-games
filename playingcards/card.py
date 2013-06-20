
class Card:
	"""Playing Card"""
	RANKS=13
	SUITS=4
	ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
	ACE=0
	JCK=10
	QN=11
	KNG=12
	suits = ['spades', 'clubs', 'diamonds', 'hearts']
	SPDS=0
	CLBS=1
	DMDS=2
	HRTS=3
	def __init__(self,rank,suit):
		self.rank = Card.ranks[rank]
		self.suit = Card.suits[suit]
	
	def to_rank_name(self):
		name = Card.ranks[self.rank]
		return name
	
	def __str__(self):
		return str(self.rank) + ' of ' + str(self.suit)
	
	def eq_rank(self,o):
		return self.rank == o.rank
	def le_rank(self,o):
		return self.rank <= o.rank
	def ge_rank(self,o):
		return self.rank >= o.rank
		
	def __eq__(self,o):
		return self.rank == o.rank and self.suit == o.suit
	
	def __ne__(self,o):
		return not self.__eq__(o)
	
	def __lt__(self,o):
		return self.rank < o.rank
	
	def __gt__(self,o):
		return self.rank > o.rank
	
	def __le__(self,o):
		return self.rank < o.rank or self.__eq__(o)

	def __ge__(self,o):
		return self.rank > o.rank or self.__eq_(o)
