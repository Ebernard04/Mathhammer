import random
import numpy as np

class weapon:
    def __init__(self, range, attacks, skill, strength, penetration, damage):
        self = self
        self.range = range
        self.attacks = attacks
        self.skill = skill
        self.strength = strength
        self.penetration = penetration
        self.damage = damage

    def basic_hit(self, modifier):
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
            elif (reroll_hit):
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
                elif(reroll_wound):
                    wval=self.wound(self,wound_modifier,toughness)
                    if(wval):
                        numwounds+=1
        return numwounds
                    
    def roll_out_hits(self, modifier, reroll_ones = False, reroll_all = False, sustained = False, lethal = False, fish = False, crit = 6):
        raw = np.zeros(self.attacks, dtype = np.int64)
        for x in range(raw.size):
            raw[x] = random.randint(1,6)
        raw_sorted = np.sort(raw)
        goal = self.skill + modifier
        if(fish):
            if(reroll_all):
                reroll = raw_sorted[raw_sorted<crit]
                num = raw_sorted.size
                for y in range(num):
                    raw_sorted[y] = random.randint(1,6)
                raw = raw_sorted
                raw_sorted = np.sort(raw)
            elif(reroll_ones):
                reroll = raw_sorted[raw_sorted<=1]
                num = raw_sorted.size
                for y in range(num):
                    raw_sorted[y] = random.randint(1,6)
                raw = raw_sorted
                raw_sorted = np.sort(raw)
        elif(reroll_all):
            reroll = raw_sorted[raw_sorted<goal]
            num = raw_sorted.size
            for y in range(num):
                raw_sorted[y] = random.randint(1,6)
            raw = raw_sorted
            raw_sorted = np.sort(raw)
        elif(reroll_ones):
            reroll = raw_sorted[raw_sorted<=1]
            num = raw_sorted.size
            for y in range(num):
                raw_sorted[y] = random.randint(1,6)
            raw = raw_sorted
            raw_sorted = np.sort(raw)
        hits = raw_sorted[raw_sorted>=goal]
        hit_num = hits.size
        if(sustained):
            sus = hits[hits>=crit]
            num_sus = sus.size
            hit_num += num_sus
        results = np.array([hit_num,0], dtype = np.int64)
        if(lethal):
            leth = hits[hits>=crit]
            num_leth = leth.size
            results[1]=num_leth
        return results
    
    def roll_out_wounds(self, toughness, modifier, reroll_ones = False, reroll_all = False, devastating = False, fish = False, hits = 0, crit = 6):
        raw = np.zeros(hits, dtype = np.int64)
        if(hits==0):
            return 0
        for x in range(raw.size):
            raw[x] = random.randint(1,6)
        raw_sorted = np.sort(raw)
        goal = 4
        if(self.strength==toughness):
            goal=4
        elif(self.strength<toughness):
            if(self.strength*2<toughness):
                goal = 6
            else:
                goal = 5
        else:
            if(self.strength>toughness*2):
                goal = 2
            else:
                goal = 3
        goal += modifier
        if(fish):
            if(reroll_all):
                reroll = raw_sorted[raw_sorted<crit]
                num = raw_sorted.size
                for y in range(num):
                    raw_sorted[y] = random.randint(1,6)
                raw = raw_sorted
                raw_sorted = np.sort(raw)
            elif(reroll_ones):
                reroll = raw_sorted[raw_sorted<=1]
                num = raw_sorted.size
                for y in range(num):
                    raw_sorted[y] = random.randint(1,6)
                raw = raw_sorted
                raw_sorted = np.sort(raw)
        elif(reroll_all):
            reroll = raw_sorted[raw_sorted<goal]
            num = raw_sorted.size
            for y in range(num):
                raw_sorted[y] = random.randint(1,6)
            raw = raw_sorted
            raw_sorted = np.sort(raw)
        elif(reroll_ones):
            reroll = raw_sorted[raw_sorted<=1]
            num = raw_sorted.size
            for y in range(num):
                raw_sorted[y] = random.randint(1,6)
            raw = raw_sorted
            raw_sorted = np.sort(raw)
        wounds = raw_sorted[raw_sorted>=goal]
        wound_num = wounds.size
        results = np.array([wound_num,0],dtype=np.int64)
        if(devastating):
            dev = wounds[wounds>=crit]
            num_dev = dev.size
            results[1] = num_dev
        return results
        


