from Sourcecode import *
import dearpygui.dearpygui as dpg


def create_default_weapons():
    res = [close_combat_weapon(),bolt_pistol()]
    return res

default_weap = create_default_weapons()

def main():
    
    dpg.create_context()
    dpg.create_viewport(title='Simulator Tester', width=1600, height=1600)

    with dpg.window(label="Model Stats",width=800, height=1600, pos=[800,0]):
        def model_callback(sender, app_data, user_data):
            print("model created")
        dpg.add_text("Enter Stats For your model:")
        #stats
        faction = dpg.add_input_text(label="Faction", default_value="faction")
        Mname = dpg.add_input_text(label="Name", default_value="Model 1")
        movem = dpg.add_input_int(label="Movement",min_value=1,default_value=1)
        toughness = dpg.add_input_int(label="Toughness",min_value=1,default_value=1)
        save = dpg.add_input_int(label="Save",min_value=2, max_value=6,default_value=2)
        wounds = dpg.add_input_int(label="Wounds",min_value=1,default_value=1)
        leadership = dpg.add_input_int(label="Leadership",min_value=2,default_value=1)
        OC = dpg.add_input_int(label="Objective Control",min_value=1,default_value=1)
        weap = dpg.add_combo(tag = "dropdown", label = "Weapon", items = default_weap)
        #creation
        dpg.add_button(label="Create Model", callback= model_callback, user_data=[faction,Mname,movem,toughness,save,wounds,leadership,OC,weap])

    with dpg.window(label="Weapon Stats",width=800, height=1600):
        def weapon_callback(sender, app_data, user_data):
            weapon_attributes = {"assault": False,
                                    "rapid fire": False,
                                    "ignores cover": False,
                                    "twin-linked": False,
                                    "pistol": False,
                                    "torrent": False,
                                    "lethal": False,
                                    "lance": False,
                                    "indirect fire": False,
                                    "precision": False,
                                    "blast": False,
                                    "heavy": False,
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
            default_weap.append(weapon(user_data[6],user_data[0],user_data[1],user_data[2],user_data[3],user_data[4],user_data[5],weapon_attributes))
            weap.__setattr__("item", default_weap)
            #print(default_weap)
            print("weapon created")
        dpg.add_text("Enter Stats For your weapon:")
        #stats
        range = dpg.add_input_int(label="Range - 0 for melee",min_value=0,default_value=0)
        attacks = dpg.add_input_int(label="Attacks",min_value=1,default_value=1)
        skill = dpg.add_input_int(label="Skill",min_value=2, max_value=6,default_value=2)
        strength = dpg.add_input_int(label="Strength",min_value=1,default_value=1)
        pen = dpg.add_input_int(label="Armour Penetration",min_value=1,default_value=1)
        damage = dpg.add_input_int(label="Damage",min_value=1,default_value=1)
        #label
        Wname = dpg.add_input_text(label="Name", default_value="Weapon 1")
        #creation
        dpg.add_button(label="Create Weapon", callback= weapon_callback, user_data=[range,attacks,skill,strength,pen,damage,Wname])
        
        
   
        
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__== "__main__" :
    main()