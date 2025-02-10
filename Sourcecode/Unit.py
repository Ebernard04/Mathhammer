import weapon
import numpy as np
import random
import math

class Unit:
    def __init__(self, faction, name, movement, toughness, save, wound, leadership, objective_control, battleshocked, alive=True):
        self.faction = faction
        self.name = name
        self.movement = movement
        self.toughness = toughness
        self.save = save
        self.wound = wound
        self.leadership = leadership
        self.objective_control = objective_control
        self.battleshocked = battleshocked
        self.alive = alive

    def roll_save(self, wounds, pen, modifiers, invuln = False, invuln_value=6, crit = 6, reroll_ones = False, reroll_all = False, crit_effect = False):
        mod = self.save
        mod += modifiers
        mod -= pen
        goal = mod
        if(invuln):
            goal = min(goal,invuln_value)
        raw = np.zeros(wounds, dtype = np.int64)
        for x in range(raw.size):
            raw[x] = random.randint(1,6)
        raw_sorted = np.sort(raw)
        if(goal > 6):
            c_data = raw_sorted[raw_sorted>=crit]
            c_num = c_data.size
            res = np.array([wounds,0])
            if(crit_effect):
                res[1]=c_num
            return res
        if(reroll_all):
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
        fails = raw_sorted[raw_sorted<goal]
        num_fails = fails.size
        res = np.array([num_fails,0])
        if(crit_effect):
            crits = raw_sorted[raw_sorted>=crit]
            crit_num = crits.size
            res[1]=crit_num
        return res
    
    def takeWound(self, wounds, damage):
        if(not self.alive):
           res = np.array([False,wounds,damage])
           return res
        elif(wounds*damage >= self.wound):
            self.alive = False
            shots_required = math.ceil(self.wound,damage) #use ceiling essentially gives number of instances of damage required to equal or surpass self.wound
            shots_remaining = wounds-shots_required
            res = np.array([False,shots_remaining,damage])
        else:
            dmg = wounds*damage
            hp_left = self.wound - dmg
            self.wound = hp_left
            res = np.array([True,0,damage])

            