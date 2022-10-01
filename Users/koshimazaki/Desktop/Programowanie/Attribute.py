from Effect import Effect

class Attribute:
	def __init__(self,name,description,attackStyle):
		self.name = name
		self.description = description
		self.devlev = 1
		self.attackStyle = attackStyle
		self.effects = []

	def devlev_up(self,value):
		self.devlev += value

	def add_effect(self,effect):
		if self.devlev <= len(self.effects):
			return 0
		else:
			self.effects += [effect.name]

	def show_status(self):
		print(f"{self.attackStyle} {self.name}\n{self.description}\nDevlev: {self.devlev}\nEffects: {self.effects}\n")

