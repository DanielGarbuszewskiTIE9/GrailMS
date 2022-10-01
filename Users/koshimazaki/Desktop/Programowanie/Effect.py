class Effect:
	def __init__(self,name,affection,value,multiplier):
		self.name = name
		self.affection = affection
		self.value = value
		self.multiplier = multiplier
	
	def upgrade(self):
		self.value *= self.multiplier
