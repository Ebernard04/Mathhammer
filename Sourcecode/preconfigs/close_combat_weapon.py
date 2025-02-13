import Sourcecode.classes.weapon as weapon

class close_combat_weapon(weapon):
    def __init__(self):
        weapon_attributes = {
                            "assault": False,
                            "rapid fire": False,
                            "ignores cover": False,
                            "twin-linked": False,
                            "pistol": False,
                            "torrent": False,
                            "lethal": False,
                            "lance": False,
                            "indirect fire": False,
                            "precision": False,
                            "blast": False,
                            "heavy": False,
                            "hazardous": False,
                            "devastating": False,
                            "sustained": False,
                            "extra attacks": False,
                            "anti-infantry": False,
                            "anti-monster": False,
                            "anti-vehicle": False,
                            "anti-mounted": False,
                            "anti-psyker": False
                        }
        super.__init__(1,3,3,4,0,1,weapon_attributes,0,0)