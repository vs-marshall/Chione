from modules.autoclicker import thread_lclick, thread_rclick
from modules.movement import thread_autosprint, thread_wtap, thread_strafing
from modules.misc import thread_antiafk, selfdestruct
from modules.configs import save_config, load_config
from modules.settings import thread_window, thread_menu, hide_taskbar, dis_tooltips, on_top, reset_settings
from config.categories import ModuleCategory as MC

modules = {
    "LeftClicker": {
        "name": "LeftClicker",
        "category": MC.COMBAT,
        "hotkey": True,
        "toggle": True,
        "slider": 3,
        "slider_min1": 1,
        "slider_max1": 40,
        "slider_text1": "CPS:",
        "slider_step1": 1,
        "slider_default1": 20,
        "slider_tooltip1": "Leftclicks per second.",
        "slider_min2": 0,
        "slider_max2": 10,
        "slider_text2": "Randomize:",
        "slider_step2": 1,
        "slider_default2": 2,
        "slider_tooltip2": "Randomize the Clicks.",
        "slider_min3": 0,
        "slider_max3": 10,
        "slider_text3": "Shake:",
        "slider_step3": 1,
        "slider_default3": 2,
        "slider_tooltip3": "Shake the mouse while leftclicking.",
        "checkbox": 2,
        "checkbox_text1": "Hold Leftclick",
        "checkbox_tooltip1": "Click while holding leftclick.",
        "checkbox_text2": "Blockhit",
        "checkbox_tooltip2": "Enable blockhit in one second intervals.",
        "params": ["get_slider_value", "get_slider_value", "get_slider_value", "get_checkbox_value", "get_checkbox_value"], 
        "command": thread_lclick
    },
    "RightClicker": {
        "name": "RightClicker",
        "category": MC.COMBAT,
        "hotkey": True,
        "toggle": True,
        "slider": 3,
        "slider_min1": 1,
        "slider_max1": 40,
        "slider_text1": "CPS:",
        "slider_step1": 1,
        "slider_default1": 15,
        "slider_tooltip1": "Rightclicks per second.",
        "slider_min2": 0,
        "slider_max2": 10,
        "slider_text2": "Randomize:",
        "slider_step2": 1,
        "slider_default2": 2,
        "slider_tooltip2": "Randomize the Clicks.",
        "slider_min3": 0,
        "slider_max3": 10,
        "slider_text3": "Shake:",
        "slider_step3": 1,
        "slider_default3": 2,
        "slider_tooltip3": "Shake the mouse while rightclicking.",
        "checkbox": 1,
        "checkbox_text1": "Hold Rightclick",
        "checkbox_tooltip1": "Click while holding rightclick.",
        "params": ["get_slider_value", "get_slider_value", "get_slider_value", "get_checkbox_value"], 
        "command": thread_rclick
    },
    "AutoSprint": {
        "name": "AutoSprint",
        "category": MC.MOTION,
        "hotkey": True,
        "toggle": True,
        "params": [],
        "command": thread_autosprint
    },
    "W-Tap": {
        "name": "W-Tap",
        "category": MC.MOTION,
        "hotkey": True,
        "toggle": True,
        "slider": 3,
        "slider_min1": 0.01,
        "slider_max1": 1,
        "slider_text1": "Delay:",
        "slider_step1": 0.01,
        "slider_default1": 0.25,
        "slider_tooltip1": "The delay between each W-Tap.",
        "slider_min2": 0.00,
        "slider_max2": 0.20,
        "slider_text2": "Randomize:",
        "slider_step2": 0.01,
        "slider_default2": 0.10,
        "slider_tooltip2": "Randomize the delay.",
        "slider_min3": 0.00,
        "slider_max3": 0.50,
        "slider_text3": "Hold:",
        "slider_step3": 0.01,
        "slider_default3": 0.15,
        "slider_tooltip3": "The time the W-Key will be held.",
        "params": ["get_slider_value", "get_slider_value", "get_slider_value"], 
        "command": thread_wtap
    },
    "Strafing": {
        "name": "Strafing",
        "category": MC.MOTION,
        "hotkey": True,
        "toggle": True,
        "slider": 3,
        "slider_min1": 0.01,
        "slider_max1": 1,
        "slider_text1": "Delay:",
        "slider_step1": 0.01,
        "slider_default1": 0.25,
        "slider_tooltip1": "The delay between each strafe.",
        "slider_min2": 0.00,
        "slider_max2": 0.20,
        "slider_text2": "Randomize:",
        "slider_step2": 0.01,
        "slider_default2": 0.10,
        "slider_tooltip2": "Randomize the delay.",
        "slider_min3": 0.00,
        "slider_max3": 0.50,
        "slider_text3": "Hold:",
        "slider_step3": 0.01,
        "slider_default3": 0.15,
        "slider_tooltip3": "The time the strafe will be held.",
        "params": ["get_slider_value", "get_slider_value", "get_slider_value"], 
        "command": thread_strafing
    },
    "AntiAFK": {
        "name": "AntiAFK",
        "category": MC.MISC,
        "hotkey": True,
        "toggle": True,
        "slider": 2,
        "slider_min1": 1,
        "slider_max1": 120,
        "slider_text1": "Timer:",
        "slider_default1": 60,
        "slider_tooltip1": "The time in seconds before the player will be moved.",
        "slider_min2": 1,
        "slider_max2": 20,
        "slider_text2": "Randomize:",
        "slider_default2": 10,
        "slider_tooltip2": "Randomize the timer.",
        "params": ["get_slider_value", "get_slider_value"],
        "command": thread_antiafk
    },
    "SelfDestruct": {
        "name": "SelfDestruct",
        "category": MC.MISC,
        "hotkey": True,
        "toggle": True,
        "checkbox": 1,
        "checkbox_text1": "Delete everything",
        "checkbox_tooltip1": "Check this to also delete all config files and the program itself.",
        "params": ["get_checkbox_value"],
        "command": selfdestruct
    },
    "LoadConfig": {
        "name": "Load Config",
        "category": MC.CONFIG,
        "hotkey": False,
        "toggle": False,
        "label": 1,
        "label_text1": "Load the settings from one of your saved config-files.",
        "button": 1,
        "button_img1": "Load",
        "button_params1": [],
        "button_command1": load_config
    },
    "SaveConfig": {
        "name": "Save Config",
        "category": MC.CONFIG,
        "hotkey": False,
        "toggle": False,
        "label": 1,
        "label_text1": "Save your current settings to a config-file.",
        "button": 1,
        "button_img1": "Save",
        "button_params1": [],
        "button_command1": save_config
    },
    "General": {
        "name": "General",
        "category": MC.SETTINGS,
        "hotkey": False,
        "toggle": False,
        "checkbox": 5,
        "checkbox_text1": "Hide from Taskbar",
        "checkbox_tooltip1": "Hide the program from the taskbar.",
        "checkbox_command1": hide_taskbar,
        "checkbox_text2": "Disable Tooltips",
        "checkbox_tooltip2": "Disable all tooltips.",
        "checkbox_command2": dis_tooltips,
        "checkbox_text3": "Pause in Menu",
        "checkbox_tooltip3": "Pause all modules when in the game menu, inv. or chat.",
        "checkbox_command3": thread_menu,
        "checkbox_text4": "Only in Focus",
        "checkbox_tooltip4": "Pause all modules when the focussed window is not Minecraft.",
        "checkbox_command4": thread_window,
        "checkbox_text5": "Always on Top",
        "checkbox_tooltip5": "Keep the program always on top.",
        "checkbox_command5": on_top,
        "button": 1,
        "button_text1": "Reset Program",
        "button_tooltip1": "Reset & closes the program. May help with some bugs.",
        "button_command1": reset_settings
    },
    "About": {
        "name": "About",
        "category": MC.SETTINGS,
        "hotkey": False,
        "toggle": False,
        "label": 4,
        "label_text1": "Chione is a python-based, free and open-source autoclicker and macro assistant. Be aware that using this software may be prohibited by some servers. Use at your own risk.",
        "label_text2": "If you find any bugs or have suggestions, please report them to the GitHub page:\n'vs-marshall/Chione'",
        "label_link2": "https://github.com/vs-marshall/Chione",
        "label_text3": "Discord:\n'marshall.com'",
        "label_link3": "https://discord.gg/HpA7JdP3uq",
        "label_text4": "GitHub:\n'vs-marshall'",
        "label_link4": "https://github.com/vs-marshall"
    }
}