import Sourcecode.classes.Model as Model
import Sourcecode.classes.Unit as Unit
import Sourcecode.preconfigs.bolt_pistol as bolt_pistol
import Sourcecode.preconfigs.bolt_rifle as bolt_rifle
import Sourcecode.preconfigs.close_combat_weapon as close_combat_weapon
import Sourcecode.preconfigs.intercessor as intercessor

class intercessor_squad(Unit):
    def __init__(self):
        models = tuple([intercessor(),intercessor(),intercessor(),intercessor(),intercessor()])
        Unit.__init__(self,5,models)