import random
import os
import time
from color import COLOR

os.system("")

# functions for menus
def Shop():
        print("╒═══════════════════════════════════════════╕")
        print("|                   STORE                   |")
        print("├───────────────────────────────────────────┤")
        print("|        (Type the number/letter of         |")
        print("|           what you'd like to do)          |")
        print("╞═══════════════════════════════════════════╡")
        print("| 1. Go to regular store                    |")
        print("| 2. ")

        text = input("[SHOP] > ")
        ClearLines()


def ClearLines():
        global clearLines
        if (clearLines): os.system("cls")


# constant vars
mispellMessages = ["You fool.", "Moron.", "Imbecile.", "Don't let it happen again.", "Clusmy, aren't you?", "Great job, moron."]

# game vars
running = True

bavis = 0
multiplier = 1
life = 3

clearLines = False

# game
while running:
        text = input("> ")
        ClearLines()
        
        if (text == "bavis"):
                bavis += 1 * multiplier
                print(f"Bavis: {bavis}")

        elif (text == "shop"):
                Shop()