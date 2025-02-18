import Sourcecode.classes.weapon as weapon

class bolt_rifle(weapon):
    def __init__(self):
        weapon_attributes = {"assault": True,
                            "rapid fire": False,
                            "ignores cover": False,
                            "twin-linked": False,
                            "pistol": True,
                            "torrent": False,
                            "lethal": False,
                            "lance": False,
                            "indirect fire": False,
                            "precision": False,
                            "blast": False,
                            "heavy": True,
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
        weapon.__init__(self,"Bolt Rifle", 24, 2, 3, 4, 1, 1,weapon_attributes,0,0)

    