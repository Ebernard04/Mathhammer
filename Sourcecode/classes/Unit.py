import Sourcecode.classes.Model as Model
import numpy as np


class Unit:
    def __init__(self, max_size, models:tuple[Model]):
        self.current_size = max_size
        self.max_size = max_size
        self.alive = True
        self.models = models #will be a tuple of models

    # Getters and Setters
    def get_current_size(self):
        return self.current_size
    
    def set_current_size(self, value):
        self.current_size = value

    def get_max_size(self):
        return self.max_size
    
    def set_max_size(self, value):
        self.max_size = value

    def get_alive(self):
        return self.alive
    
    def set_alive(self, value):
        self.alive = value

    def get_models(self):
        return self.models
    
    def set_models(self, value):
        self.models = value

    def get_toughness(self):
        return self.models[0].get_toughness()

    def attack(self, toughness, distance, hit_mod, wound_mod):
        ## array should have format [wounds, dev wounds, pen value, damage per wound]
        wounds = np.array([0,0,0,0])
        for x in self.models:
            temp = x.attack(toughness, hit_mod, wound_mod, distance)
            wounds[0]+=temp[0]
            wounds[1]+=temp[1]
            wounds[2]+=temp[2]
            wounds[3]+=temp[3]
        return wounds
    
    #takes in wound modifiers and rerolls and will return fails
    def basic_save(self, wounds, pen, modifiers, reroll_ones, reroll_all):
        return self.models[-1].roll_save(wounds, pen, modifiers, reroll_ones = reroll_ones, reroll_all = reroll_all) 
    
    #takes in number of wounds and applies to unit
    def take_damage(self, wounds, damage, fnp= False, fnp_val=6):
        wounds_left = wounds
        if(self.current_size==0):
            print("unit is already dead")
        while (wounds_left > 0 and self.current_size>0):
            wl = self.models[self.current_size-1].take_wound(wounds, damage, fnp, fnp_val)
            if(not wl[0]):
                self.current_size = self.current_size-1
                wounds_left = wl[1]
        if (self.current_size <= 0):
            self.alive = False
        result = np.array([wounds_left,self.current_size]) #returns array of number of wounds left and the current size so you can determine if the unit lived

            
    #takes in array that attack function outputs
    #will process the task of doing saves and then applying damage for the unit
    #return true if unit lives, false if it dies
    def no_rr_take_attack(self, wounds, devs, pen, damage, modifiers):
        if(not self.alive):
            print("unit is already dead, you did overkill")
            return False
        fails = self.basic_save(wounds,pen,modifiers,False,False)
        shots = fails[0]+devs
        res = self.take_damage(shots,damage,False,6)
        if(res[1]<=0):
            print("you have killed the unit with a leftover %s shots"%res[0])
            return False
        else:
            print("The unit has lived with %s models"%self.current_size)