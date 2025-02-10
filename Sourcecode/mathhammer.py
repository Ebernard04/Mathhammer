

def hitChecker(roll, check):
    return (roll >= check)


def woundChecker(roll, strength, toughness):
    if(strength == toughness):
        return roll>=4
    else:
        if(strength > toughness):
            if(strength > (2*toughness)):
                return roll>=2
            else:
                return roll>=3 
        else:
            if(strength < toughness):
                if((2*strength) < toughness):
                    return roll>=6
                else:
                    return roll>=5
        
    

