from Sourcecode import *
import dearpygui.dearpygui as dpg
import copy

#function to instanciate default weapons for use
def create_default_weapons():
    res = [close_combat_weapon(),bolt_pistol(),boltgun(),bolt_rifle()]
    return res
#function to create default models for use
def create_default_models():
    res = [intercessor()]
    return res

#function to create default units for use
def create_default_units():
    res = [intercessor_squad()]
    return res

#list of the default weapons (will be where all weapons are added)
weapons = create_default_weapons()
#list of default models (will be where all models are added)
models_yup = create_default_models()
#list of default units (will be where all units are added)
unit_list = create_default_units()

def main():
    
    dpg.create_context()
    dpg.create_viewport(title='Simulator Tester', width=1600, height=800)

    with dpg.window(label="Simulation Settings", width=800, height=400, pos=[800,400]):
        def sim_callback(sender, app_data, user_data):
            tough = 3#user_data[1].get_toughness()
            print(user_data)
            #r = user_data[2]
            #for x in range(0,r):
            dealt = user_data[0].attack(tough, user_data[3], 0, 0)
            print(dealt)
        dpg.add_text("Select your units:")
        atk = dpg.add_combo(label = "Attackers", items = unit_list)
        tgt = dpg.add_combo(label = "Target", items = unit_list)
        sim = dpg.add_input_int(label = "Number of simulations", default_value = 1)
        dist = dpg.add_input_double(label= "Distance between units (in inches)", default_value = 0)
        dpg.add_button(label= "Run Simulation", callback=sim_callback, user_data= [dpg.get_value(atk),dpg.get_value(tgt), dpg.get_value(sim), dpg.get_value(dist)])

    with dpg.window(label="Unit Stats", width=800, height=400, pos=[0,400]):
        def unit_callback(sender, app_data, user_data):
            m = [user_data[0]]
            x = 1
            while x < user_data[1]:
                m.append(copy.deepcopy(user_data[0]))
                x+=1
            tup = tuple(m)
            unit_list.append(Unit(user_data[1],tup))
            dpg.configure_item(atk, items=unit_list)
            dpg.configure_item(tgt, items=unit_list)
        dpg.add_text("Unit things here:")
        mods = dpg.add_combo(label = "Model", items = models_yup)
        size = dpg.add_input_int(label = "Number of models", min_value=1, default_value=1)
        dpg.add_button(label="Create Unit",callback = unit_callback, user_data=[dpg.get_value(mods),dpg.get_value(size)])

    with dpg.window(label="Model Stats",width=800, height=400, pos=[800,0]):
        def model_callback(sender, app_data, user_data):
            models_yup.append(Model(user_data[0],user_data[1],user_data[2],user_data[3],user_data[4],user_data[5],user_data[6],user_data[7],False,[],user_data[8]))
            dpg.configure_item(mods,items=models_yup)
        dpg.add_text("Enter Stats For your model:")
        #stats
        faction = dpg.add_input_text(tag="mFaction", label="Faction", default_value="faction")
        Mname = dpg.add_input_text(tag="Mname", label="Name", default_value="Model 1")
        movem = dpg.add_input_int(tag="move", label="Movement",min_value=1,default_value=1)
        toughness = dpg.add_input_int(tag="tough", label="Toughness",min_value=1,default_value=1)
        save = dpg.add_input_int(tag="save", label="Save",min_value=2, max_value=6,default_value=2)
        wounds = dpg.add_input_int(tag="wound", label="Wounds",min_value=1,default_value=1)
        leadership = dpg.add_input_int(tag="leader", label="Leadership",min_value=2,default_value=1)
        oc = dpg.add_input_int(tag="oc", label="Objective Control",min_value=1,default_value=1)
        weap = dpg.add_combo(tag = "dropdown", label = "Weapon", items = weapons)
        #creation
        dpg.add_button(label = "Create Model",
                       callback = model_callback,
                       user_data = [dpg.get_value(faction),
                                    dpg.get_value(Mname),
                                    dpg.get_value(movem),
                                    dpg.get_value(toughness),
                                    dpg.get_value(save),
                                    dpg.get_value(wounds),
                                    dpg.get_value(leadership),
                                    dpg.get_value(oc),
                                    dpg.get_value(weap)])

    with dpg.window(label="Weapon Stats",width=800, height=400):
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
            weapons.append(weapon(user_data[6],user_data[0],user_data[1],user_data[2],user_data[3],user_data[4],user_data[5],weapon_attributes))
            #weap.__setattr__("item", default_weap)
            print(user_data[6])
            print(weapons[-1].get_name())
            print("weapon created")
            dpg.configure_item(weap,items=weapons)
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
        dpg.add_button(label="Create Weapon", 
                       callback= weapon_callback, 
                       user_data=[dpg.get_value(range),
                                  dpg.get_value(attacks),
                                  dpg.get_value(skill),
                                  dpg.get_value(strength),
                                  dpg.get_value(pen),
                                  dpg.get_value(damage),
                                  dpg.get_value(Wname)])
        
   
   
        
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__== "__main__" :
    main()