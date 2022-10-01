from Attribute import Attribute
from Effect import Effect

class Technique:
	def __init__(self,name,description,spirit):
		self.name = name
		self.description = description
		self.spirit = spirit
		self.devlev = 1
		self.attributes = []

	def devlev_up(self,value):
		self.devlev += value

	def add_attribute(self,attribute):
		if self.devlev <= len(self.attributes):
			return 0
		else:
			self.attributes += [attribute.name]

	def show_status(self):
		print(f"{self.name} technique of the {self.spirit} spirit\n{self.description}\nDevlev: {self.devlev}\nAttributes: {self.attributes}\n")


