import rbtree

class Hand:
	"""Hand of playing cards"""
	def __init__(self):
		self.cards = rbtree.rbtree()
	
	def add(self,card):
		if card in self.cards:
			self.cards[card]+=1
		else:
			self.cards[card]=1

	def remove(self,card):
		if card in self.cards:
			self.cards[card]-=1
			if self.cards[card]==0:
				del self.cards[card]
		
	
	def clear(self):
		self.cards.clear()
	
	def __getitem__(self,idx):
		itr = iter(self.cards)
		itr.goto(idx-1)
		return itr.next()
#	def __setitem__(self,idx):
	
	def __len__(self):
		return len(self.cards)
	def __str__(self):
		s = '['
		#itr = iter(self.cards)
		for card, num in self.cards.iteritems():
			s += '(' + str(card) + ',' + str(num) + '), '
		return s+']'
