#import Sourcecode.classes.Model as model
#import Sourcecode.classes.weapon as weapon
#import Sourcecode.preconfigs.bolt_pistol as bp
#import Sourcecode.preconfigs.close_combat_weapon as ccw
import dearpygui.dearpygui as dpg

def main():
    dpg.create_context()
    dpg.create_viewport(title='Simulator Tester', width=1600, height=1600)
    with dpg.window(label="Weapon Stats",width=1600, height=1600):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Save")
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
        dpg.add_input_int(label="Attacks",min_value=1)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__== "__main__" :
    main()