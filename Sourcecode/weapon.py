import random
import numpy as np
import math

#class that handles weapons themselves and thus hit and wound rolls
class weapon:
    #constructor, most are basic stats from weapons' datasheet
    #abilities is a dict of booleans to say if a weapon has that ability. options are listed below:
    #assault, rapid fire, ignores cover, twin-linked, pistol, torrent, lethal, lance, indirect fire, 
    #precision, blast, heavy, hazardous, devastating, sustained, extra attacks, anti-infantry, anti-monster,
    #anti-vehicle, anti-mounted, anti-psyker
    #sustained_val denotes the number of hits added on a sustained hit -> defaults to 0 for weapons without sustained hits
    def __init__(self, range, attacks, skill, strength, penetration, damage, abilites:dict[str,bool], sustained_val = 0, rapid_val = 0):
        self = self
        self.range = range
        self.attacks = attacks
        self.skill = skill
        self.strength = strength
        self.penetration = penetration
        self.damage = damage
        self.abilities = abilites
        self.sustained_val = sustained_val
        self.rapid_val = rapid_val
                    
    #function to roll to hit on weapon
    # takes in modifier for hitting and then a decent amount of other characteristics   
    # fish tells you if you will reroll all non critical hits that you can vs only rerolling non hits if able 
    # needs distance value to tell you if rapid fire goes off
    # 
    # sustained denotes critical hits which add an amount of additional hits denoted by amount of sustained value
    # lethal hits are removed from number of hits
    # lethal hits denotes critical hits which due to the lethal hits ability automatically wound without needed a roll    
    # additionally has a crit value passed in case a weapon or attack modifies this
    # 
    # returns a numpy array in the format [number of hits, lethal hits]        
    def hit_roll(self, modifier, distance, reroll_ones = False, reroll_all = False, sustained = False, sustained_val = 0, lethal = False, fish = False, crit = 6):
        #generate an array and fill it with random values from 1 to 6 inclusive to simulate dice being rolled
        #array is sized based on the attacks characteristic of the weapon
        atk = self.attacks
        if(self.abilities["rapid fire"]):
            if(distance <= (self.range/2)):
                atk+=self.rapid_val

        raw = np.random.randint(1,7,size=atk, dtype=np.int64)
        #sort rolls for easy manipulation
        raw_sorted = np.sort(raw)
        #value needed for a sucessful hit is calculated
        goal = self.skill + modifier
        goal = min(goal,6) #raw 6s always hit
        if(fish): #if fishing then reroll all non crits that you are able 
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
        elif(reroll_all): #if not fishing reroll all non hits if able ---- rerolling all hits does not stack with rerolling ones to give multiple rerolls
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
        #determine number of rolls larger than the goal value
        hits = raw_sorted[raw_sorted>=goal]
        hit_num = hits.size
        if(sustained): #add in additional hits based on the number of crits and the sustained val
            sus = hits[hits>=crit]
            num_sus = sus.size
            num_add = num_sus * sustained_val
            hit_num += num_add
        results = np.array([hit_num,0], dtype = np.int64) #results array of format [hits, lethal hits]
        if(lethal): #determine lethal hits
            leth = hits[hits>=crit]
            num_leth = leth.size
            results[0]-=num_leth #remove lethals from hits
            results[1]=num_leth #denote number of lethals
        return results
    


    # function to simulate the rolling of a wound roll
    # toughness denotes the toughness of the target
    # modifier denotes modifier to wound roll
    # devastating hits are crits which target cannot save
    # hits denotes number of rolls to be done
    # returns array of [number of wounds, number of dev wounds] -> dev wounds are removed from normal wounds to avoid double count
    def wound_roll(self, toughness, modifier, reroll_ones = False, reroll_all = False, devastating = False, fish = False, hits = 0, crit = 6):
        if(hits==0): #edge case for situation where function is asked to roll 0 dice
            return 0
        raw = np.random.randint(1,7,size=hits, dtype=np.int64)
        raw_sorted = np.sort(raw)
        goal = 4 #default value for goal of just strength and toughness are equal
        if(self.strength==toughness):
            goal=4
        elif(self.strength<toughness): #if toughness exceeds strength then 5, if toughness exceeds 2x strength then 6
            if(self.strength*2<toughness):
                goal = 6
            else:
                goal = 5
        else:
            if(self.strength>toughness*2): #if strength exceeds toughness then 3, if strength exceeds 2x toughness then 2
                goal = 2
            else:
                goal = 3
        goal += modifier #apply modifier
        goal = min(goal, 6) #raw 6s always wound
        if(fish): #same fishing and reroll logic as in hit roll function
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
        wounds = raw_sorted[raw_sorted>=goal] #values which are higher than goal become wounds
        wound_num = wounds.size
        results = np.array([wound_num,0],dtype=np.int64)
        if(devastating):
            dev = wounds[wounds>=crit]
            num_dev = dev.size
            results[0] -= num_dev
            results[1] = num_dev
        return results #returns array of [number of wounds, number of dev wounds]
    


    def use(self, hit_modifier, wound_modifier, toughness, distance, reroll_hit = False, reroll_wound = False, reroll_hit_ones = False, reroll_wound_ones = False, fish_hits = False, fish_wounds = False, crit = 6, sustained = False, lethal = False, devastating = False, sustained_value = 0):
        sus = False
        leth = False
        dev = False
        sus = (self.abilities["sustained"] or sustained)
        leth = (self.abilities["lethal"] or lethal)
        dev = (self.abilities["devastating"] or devastating)
        sus_val = max(self.sustained_val,sustained_value)
        
        hit_data = self.hit_roll(hit_modifier, distance,reroll_hit_ones, reroll_hit, sus, sus_val, leth, fish_hits, crit) ##returns array of [hits, lethals]
        wound_data = self.wound_roll(toughness,wound_modifier,reroll_wound_ones,reroll_wound,dev,fish_wounds,hit_data[0],crit) ## returns array of [wounds, dev wounds]
        if(leth):
            wound_data[0]+=hit_data[1] #if lethal hits add lethal hits onto wounds to be saved
        atk_data = np.array([self.penetration,self.damage]) #temp array with value of AP and damage to be passed forward
        output = np.append(wound_data,atk_data) ## array should have format [wounds, dev wounds, pen value, damage per wound]
        return output

    def getRange(self): #return range attribute
        return self.range