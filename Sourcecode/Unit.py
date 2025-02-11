import Model
import numpy as np


class Unit:
    def __init__(self, size, models:list[Model.Model]):
        self.size = size
        self.models = self.models #will be a list of models

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
    
    def save(self, wounds, pen, modifiers, reroll_ones, reroll_all):
        self.models[0].roll_save(wounds, pen, modifiers, invuln, invuln_value, crit, reroll_ones, reroll_all, crit_effect)