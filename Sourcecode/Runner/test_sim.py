from Sourcecode import *
import dearpygui.dearpygui as dpg

def create_default_weapons():
    res = [close_combat_weapon(),bolt_pistol()]
    return res



def main():
    default_weap = create_default_weapons()
    dpg.create_context()
    dpg.create_viewport(title='Simulator Tester', width=1600, height=1600)
    with dpg.window(label="Weapon Stats",width=800, height=1600):
        dpg.add_text("Enter Stats For your weapon:")
        #stats
        dpg.add_input_int(label="Range - 0 for melee",min_value=0,default_value=0)
        dpg.add_input_int(label="Attacks",min_value=1,default_value=1)
        dpg.add_input_int(label="Skill",min_value=2, max_value=6,default_value=2)
        dpg.add_input_int(label="Strength",min_value=1,default_value=1)
        dpg.add_input_int(label="Armour Penetration",min_value=1,default_value=1)
        dpg.add_input_int(label="Damage",min_value=1,default_value=1)
        #label
        dpg.add_input_text(label="Name", default_value="Weapon 1")
        #creation
        dpg.add_button(label="Create Weapon")
        
        
    with dpg.window(label="Model Stats",width=800, height=1600, pos=[800,0]):
        dpg.add_text("Enter Stats For your model:")
        #stats
        dpg.add_input_text(label="Faction", default_value="faction")
        dpg.add_input_text(label="Name", default_value="Model 1")
        dpg.add_input_int(label="Movement",min_value=1,default_value=1)
        dpg.add_input_int(label="Toughness",min_value=1,default_value=1)
        dpg.add_input_int(label="Save",min_value=2, max_value=6,default_value=2)
        dpg.add_input_int(label="Wounds",min_value=1,default_value=1)
        dpg.add_input_int(label="Leadership",min_value=2,default_value=1)
        dpg.add_input_int(label="Objective Control",min_value=1,default_value=1)
        dpg.add_combo(label="Weapon",items=default_weap)
        #creation
        dpg.add_button(label="Create Model")
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__== "__main__" :
    main()