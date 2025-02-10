import random

class weapon:
    def __init__(self, range, attacks, skill, strength, penetration, damage):
        self = self
        self.range = range
        self.attacks = attacks
        self.skill = skill
        self.strength = strength
        self.penetration = penetration
        self.damage = damage

    def hit(self, modifier):
        roll = random.randint(1,6)
        if(modifier != 0):
            roll += modifier
        return (roll >= self.skill)
    
    def wound(self, modifier, toughness):
        roll = random.randint(1,6)
        if(modifier != 0):
            roll += modifier
        check = 4
        if(self.strength == toughness):
            check = 4
        else:
            if(self.strength > toughness):
                if(self.strength > (2*toughness)):
                    check = 2
                else:
                    check = 3
            else:
                if(self.strength < toughness):
                    if((self.strength*2) < toughness):
                        check = 6
                    else:
                        check = 5
        return (roll>=check)
    
    def use(self, hit_modifier, wound_modifier, toughness, reroll_hit = False, reroll_wound = False):
        numhits = 0
        numwounds = 0
        for x in range(self.attacks):
            hval = self.hit(self, hit_modifier)
            if (hval):
                numhits+=1
            else:
                if (reroll_hit):
                    hval = self.hit(self, hit_modifier)
                    if (hval):
                        numhits+=1
        if(numhits==0):
            return 0
        else:
            for y in range(numhits):
                wval = self.wound(self,wound_modifier,toughness)
                if(wval):
                    numwounds+=1
                else:
                    if(reroll_wound):
                        wval=self.wound(self,wound_modifier,toughness)
                        if(wval):
                            numwounds+=1
        return numwounds
                    

