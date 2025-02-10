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
                    
    def hit_roll(self, modifier, reroll_ones = False, reroll_all = False, sustained = False, lethal = False, fish = False, crit = 6):
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
    
    def wound_roll(self, toughness, modifier, reroll_ones = False, reroll_all = False, devastating = False, fish = False, hits = 0, crit = 6):
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
        
    def use(self, hit_modifier, wound_modifier, toughness, reroll_hit = False, reroll_wound = False, reroll_hit_ones = False, reroll_wound_ones = False, fish_hits = False, fish_wounds = False, crit = 6, sustained = False, lethal = False, devastating = False):
        hit_data = self.hit_roll(hit_modifier ,reroll_hit_ones, reroll_hit, sustained, lethal, fish_hits, crit) ##returns array of [hits, lethals]
        wound_data = self.wound_roll(toughness,wound_modifier,reroll_wound_ones,reroll_wound,devastating,fish_wounds,hit_data[0],crit) ## returns array of [wounds, dev wounds]
        if(lethal):
            wound_data[0]+=hit_data[1]
        atk_data = np.array([self.penetration,self.damage])
        output = np.append(wound_data,atk_data) ## array should have format [wounds, dev wounds, pen value, damage per wound]
        return output

    def getRange(self):
        return self.range