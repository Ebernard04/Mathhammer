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
        weapon.__init__(self,1,3,3,4,0,1,weapon_attributes,0,0)


    def __str__(self):
        return "Close Combat Weapon"
    def __repr__(self):
        return "Close Combat Weapon"