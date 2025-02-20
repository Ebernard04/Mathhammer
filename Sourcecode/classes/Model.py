import Sourcecode.classes.weapon as weapon
import numpy as np
import random
import math

class Model:
    #constructor using basic information from datasheets
    def __init__(self, faction, name, movement, toughness, save, wound, leadership, objective_control, battleshocked, melee:list[weapon.weapon], ranged:list[weapon.weapon], alive=True,invuln_save = False, invuln_value=6, crit_save = 6, sv_reroll_ones = False, sv_reroll_all = False, sv_crit_effect = False, fnp = False, fnp_val = 6):
        self.faction = faction
        self.name = name
        self.movement = movement
        self.toughness = toughness
        self.save = save
        self.wound = wound
        self.leadership = leadership
        self.objective_control = objective_control
        self.battleshocked = battleshocked
        self.alive = alive #bool to denote if a model is still alive
        self.melee = melee #list of melee weapons
        self.ranged = ranged #list of ranged weapons
        self.invuln_save = invuln_save #does this model have an invuln save
        self.invuln_value = invuln_value #what is the roll for the invuln save
        self.crit_save = crit_save #is there an effect on crit saves
        self.sv_reroll_ones = sv_reroll_ones #does model reroll saves of one
        self.sv_reroll_all = sv_reroll_all #does model reroll failed saves
        self.fnp = fnp #does model have a feel no pain
        self.fnp_val = fnp_val #what is the roll for feel no pain

    # Getters and Setters
    def __str__(self):
        res = "A "+ self.name + " model"
        return res
    def __repr__(self):
        return self.name

    def get_faction(self):
        return self._faction
    
    def set_faction(self, value):
        self._faction = value

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value

    def get_movement(self):
        return self._movement
    
    def set_movement(self, value):
        self._movement = value

    def get_toughness(self):
        return self._toughness
    
    def set_toughness(self, value):
        self._toughness = value

    def get_save(self):
        return self._save
    
    def set_save(self, value):
        self._save = value

    def get_wound(self):
        return self._wound
    
    def set_wound(self, value):
        self._wound = value

    def get_leadership(self):
        return self._leadership
    
    def set_leadership(self, value):
        self._leadership = value

    def get_objective_control(self):
        return self._objective_control
    
    def set_objective_control(self, value):
        self._objective_control = value

    def get_battleshocked(self):
        return self._battleshocked
    
    def set_battleshocked(self, value):
        self._battleshocked = value

    def get_alive(self):
        return self._alive
    
    def set_alive(self, value):
        self._alive = value

    def get_melee(self):
        return self._melee
    
    def set_melee(self, value):
        self._melee = value

    def get_ranged(self):
        return self._ranged
    
    def set_ranged(self, value):
        self._ranged = value

    def get_invuln_save(self):
        return self._invuln_save
    
    def set_invuln_save(self, value):
        self._invuln_save = value

    def get_invuln_value(self):
        return self._invuln_value
    
    def set_invuln_value(self, value):
        self._invuln_value = value

    def get_crit_save(self):
        return self._crit_save
    
    def set_crit_save(self, value):
        self._crit_save = value

    def get_sv_reroll_ones(self):
        return self._sv_reroll_ones
    
    def set_sv_reroll_ones(self, value):
        self._sv_reroll_ones = value

    def get_sv_reroll_all(self):
        return self._sv_reroll_all
    
    def set_sv_reroll_all(self, value):
        self._sv_reroll_all = value

    def get_fnp(self):
        return self._fnp
    
    def set_fnp(self, value):
        self._fnp = value

    def get_fnp_val(self):
        return self._fnp_val
    
    def set_fnp_val(self, value):
        self._fnp_val = value


    #function to determine how many wounds are saved vs go through
    #takes in number of wounds, armor pen, modifiers to the roll, wheter there is an invuln and reroll values
    def roll_save(self, wounds, pen, modifiers, invuln = False, invuln_value=6, crit = 6, reroll_ones = False, reroll_all = False, crit_effect = False):
        mod = self.save
        mod += modifiers #start with base save and add modifiers (negative modifiers will have negative value)
        mod -= pen #subtract the armour pen from the modified save
        goal = mod
        if(invuln or self.invuln_save) : #if there is an invuln save set the save value to whichever is lower 
            goal = min(goal,invuln_value,self.invuln_value)
        raw = np.random.randint(1,7,size=wounds,dtype=np.int64) #roll dice
        raw_sorted = np.sort(raw) #sort for ease
        if(goal > 6): #if required save is higher than 6 you auto fail every save
            c_data = raw_sorted[raw_sorted>=crit]
            c_num = c_data.size
            res = np.array([wounds,0])
            if(crit_effect):
                res[1]=c_num
            return res
        if(reroll_all): #logic for reroll fails and reroll ones
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
        fails = raw_sorted[raw_sorted<goal] #fails are rolls less than the goal
        num_fails = fails.size
        res = np.array([num_fails,0])
        if(crit_effect): #if there is an effect on critical saves, pass data on number along
            crits = raw_sorted[raw_sorted>=crit]
            crit_num = crits.size
            res[1]=crit_num
        return res #returns number of failed saves and number of crit saves if there is an effect in format [fails,crits]
    
    #function for determining the actual damage to model
    #wounds is number of attacks coming in
    #damage is damage per shot
    #fnp is feel no pain whether there is one and what value you need to succeed
    def takeWound(self, wounds, damage, fnp = False, fnp_val = 6):
        feel = (fnp or self.fnp) #determine fnp
        feel_val = min(fnp_val,self.fnp_val) #determine required roll for fnp
        if(not self.alive):
           res = np.array([False,wounds,damage])
           return res
        else:
            if(feel):
                rolls = np.random.randint(1,7,size=wounds,dtype=np.int64)
            if(wounds*damage >= self.wound):
                self.alive = False
                shots_required = math.ceil(self.wound,damage) #use ceiling essentially gives number of instances of damage required to equal or surpass self.wound
                shots_remaining = wounds-shots_required
                res = np.array([False,shots_remaining,damage])
            else:
                dmg = wounds*damage
                hp_left = self.wound - dmg
                self.wound = hp_left
                res = np.array([True,0,damage])

    def attack_melee(self, toughness, hit_mod, wound_mod, distance):## return array should have format [wounds, dev wounds, pen value, damage per wound]
        if(self.alive):
            result = np.array([0,0,0,0])
            for x in self.melee:
                temp = x.use(hit_mod, wound_mod, toughness, distance)
                result[0]+=temp[0]
                result[1]+=temp[1]
                result[2]+=temp[2]
                result[3]+=temp[3]
            return result
        else:
            return np.array([0,0,0,0])
        
    def attack_ranged(self, toughness, hit_mod, wound_mod, distance):## return array should have format [wounds, dev wounds, pen value, damage per wound]
        if(self.alive):
            result = np.array([0,0,0,0])
            for x in self.ranged:
                if(distance <= x.getRange()):
                    temp = x.use(hit_mod, wound_mod, toughness, distance)
                    result[0]+=temp[0]
                    result[1]+=temp[1]
                    result[2]+=temp[2]
                    result[3]+=temp[3]
            return result
        else:
            return np.array([0,0,0,0])
        
    def attack(self, toughness, hit_mod, wound_mod, distance):## return array should have format [wounds, dev wounds, pen value, damage per wound]
        if(distance > 1):
            return self.attack_ranged(toughness, hit_mod, wound_mod, distance)
        else:
            return self.attack_melee(toughness, hit_mod, wound_mod, distance)