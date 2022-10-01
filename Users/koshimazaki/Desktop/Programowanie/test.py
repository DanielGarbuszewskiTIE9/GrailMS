from Technique import Technique
from Attribute import Attribute
from Effect import Effect

fireDamage = Effect("Fire Damage","Fire",20,2)
x = Effect('x','x',2,2)

fireTornado = Attribute("Fire Tornado","Makes wind very hot","Ranged")
fireTornado.devlev_up(5)
fireTornado.add_effect(fireDamage)
fireTornado.add_effect(x)

hardFist = Technique("Hard Fist","A fist that can burn","Flame")
hardFist.devlev_up(5)
hardFist.add_attribute(fireDamage)
hardFist.add_attribute(fireTornado)
hardFist.show_status()

fireTornado.show_status()

input('')

