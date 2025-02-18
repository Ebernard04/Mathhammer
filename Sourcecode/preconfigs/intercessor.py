import Sourcecode.classes.Model as Model
import Sourcecode.preconfigs.bolt_pistol as bolt_pistol
import Sourcecode.preconfigs.bolt_rifle as bolt_rifle
import Sourcecode.preconfigs.close_combat_weapon as close_combat_weapon

class intercessor(Model):
    def __init__(self):
        ccw = close_combat_weapon()
        bp = bolt_pistol()
        br = bolt_rifle()
        Model.__init__(self,"Space Marine", "Intercessor", 6, 4, 3, 2, 6, 2, False, [close_combat_weapon()], [bolt_pistol(),bolt_rifle()],True,False,6,6,False,False,False,False,6)