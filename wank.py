# wank.py ===============================================================
import os
import sys
import time
 
jerks = 5
jizz_speed = 0.25
fast_stroke = 0.1
slow_stroke = 0.3
options = [fast_stroke, slow_stroke]
menu = "\nwank.py\n\n1. Fast\n2. Slow\n\nSelection: "
stroke_list = ["8====MM=D",
               "8===MM==D",
               "8==MM===D",
               "8=MM====D"]
jizz_list = ["8====MM=D-",
             "8====MM=D --",
             "8====MM=D --_",
             "8====MM=D ___"]
 
 
def get_selection(menu, options):
    # Display menu and get user selection from list of options
    sel = None
    while sel is None:
        os.system("cls" if os.name == "nt" else "clear")  
        try:
            sel = input(menu)
        except (NameError, SyntaxError):            
            pass
        if sel not in range(1, len(options)+1):
            sel = None
    selection = options[sel-1]
    return selection
 
 
# Accept command line arguments "fast" and "slow"
if len(sys.argv) == 2:
    speed = sys.argv[1].lower()
    if speed == "fast":
        stroke_speed = fast_stroke
    elif speed == "slow":
        stroke_speed = slow_stroke
    else:        
        stroke_speed = get_selection(menu, options)        
else:
    stroke_speed = get_selection(menu, options)        
 
# Wank
for jerk in range(jerks):
    for stroke in range(len(stroke_list)):
        os.system("cls" if os.name == "nt" else "clear")  
        print "\n" + stroke_list[stroke]
        time.sleep(stroke_speed)
    for putz in range(len(stroke_list)-2, 0, -1):
        os.system("cls" if os.name == "nt" else "clear")  
        print "\n" + stroke_list[putz]
        time.sleep(stroke_speed)
 
# Jizz
for spurt in range(len(jizz_list)):
    os.system("cls" if os.name == "nt" else "clear")  
    print "\n" + jizz_list[spurt]
    time.sleep(jizz_speed)
time.sleep(1)
a = raw_input("\nPress Enter")
os.system("cls" if os.name == "nt" else "clear")  
sys.exit()
