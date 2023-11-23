import random
import os
import time
from color import COLOR

os.system("")

# stores and other buy menus
def Store():
        print("╒═══════════════════════════════════════════╕")
        print("│                   STORE                   │")
        print("├───────────────────────────────────────────┤")
        print("│        (Type the number/letter of         │")
        print("│           what you'd like to do)          │")
        print("╞═══════════════════════════════════════════╡")
        print("│ 1. Go to bavis store                      │")
        print("╘═══════════════════════════════════════════╛")

        text = input("[STORE] > ")
        ClearScreen()

        if (text == "1" or text == "1."): BavisStore()

def BavisStore():
        print("╒═══════════════════════════════════════════╕")
        print("│                BAVIS STORE                │")
        print("├───────────────────────────────────────────┤")
        print("│        (Type the number/letter of         │")
        print("│           what you'd like to do)          │")
        print("╞═══════════════ MULTIPLIERS ════╤══════════╡")
        print("│ 1. 1x Multiplier               │    50b   │")
        print("│ 2. Max Multipliers             │     -    │")
        print("│ 3. User specified multipliers  │ 50b each │")
        print("╞═══════════════════ LIVES ══════╤══════════╡")
        print("│ 4. +1 life                     │     -    │")
        print("╘════════════════════════════════╧══════════╛")

        text = input("[BAVIS STORE] > ")
        ClearScreen()

        if (text == "1" or text == "1."): BuyMultiplier(0)
        if (text == "2" or text == "2."): BuyMultiplier(1)
        if (text == "3" or text == "3."): BuyMultiplier(2)
        
        if (text == "4" or text == "4."): BuyLife()

# options
def Options():
        global clearScreen

        print("╒═══════════════════════════════════════════╕")
        print("│          BAVIS SIMULATOR OPTIONS          │")
        print("├───────────────────────────────────────────┤")
        print("│        (Type the number/letter of         │")
        print("│         what you'd like to toggle)        │")
        print("╞═══════════════════════════════════════════╡")
        if (clearScreen): print(f"│ {COLOR.GREEN}1. Clear screen after input{COLOR.WHITE}               │")
        else: print(f"│ {COLOR.RED}1. Clear screen after input{COLOR.WHITE}               │")
        print("╘═══════════════════════════════════════════╛")

        text = input("[BAVIS STORE] > ")
        ClearScreen()

        if (text == "1" or text == "1."): 
                clearScreen = not clearScreen
                if (clearScreen): print(f"{COLOR.GREEN}[-] Now clearing screen after input{COLOR.WHITE}")
                else: print(f"{COLOR.RED}[-] No longer clearing screen after input{COLOR.WHITE}")

# buy functions for menus
def BuyMultiplier(type):
        global bavis
        global multiplier

        if (bavis < 50):
                print("[!] You don't have enough bavis!")
                return
        
        multBought = 0

        if (type == 0): # one multiplier
                multiplier += 1
                bavis -= 50

                multBought = 1
                        
        elif (type == 1): # max multipliers
                multAmount = int((bavis - bavis % 50) / 50)
                bavis -= multAmount * 50
                multiplier += multAmount
                
                multBought = multAmount

        elif (type == 2): # specified multipliers
                multStr = input("[MULTIPLIERS TO BUY] > ")
                if (not multStr.isdigit()):
                        print("[!] Not a valid number!")
                        return
                
                multInt = int(multStr)
                
                if (bavis < multInt * 50):
                        print("[!] You don't have enough bavis!")
                        return
                
                if (multInt == 0):
                        print("[!] You can't buy 0 multipliers!")
                        return
                
                bavis -= multInt * 50
                multiplier += multInt

                multBought = multInt

        print(f"{multBought} multiplier(s) bought! ({multiplier} now)")

def BuyLife():
        global bavis
        global life
        global totalLives
        
        cost = 35 ** (life + 1)

        if (bavis < cost):
                print(f"[!] You don't have enough bavis! ({cost} needed)")
                return

        print(f"Another life will cost you {cost} bavis. Are you sure you want to buy this? ({life} lives currently)")
        
        confirm = input("[Yes/No] > ")
        ClearScreen()

        if (confirm.lower() in ["yes", "y"]):
                bavis -= cost
                life += 1
                totalLives += 1
                print(f"+1 life ({life} now)")

        elif (confirm.lower() in ["no", "n"]):
                return
        
def HelpText():
        print("╒═══════════════════════════════════════════╕")
        print("│            BAVIS SIMULATOR HELP           │")
        print("├───────────────────────────────────────────┤")
        print("│ Type 'bavis' to increase your bavis by 1  │")
        print("│ Using 'bavis' is how you play the game    │")
        print("├───────────────────────────────────────────┤")
        print("│ Type 'shop' or 'store' to access the shop │")
        print("│ You can buy certain items in these stores │")
        print("│ Navigate around these stores using the    │")
        print("│ numbers and letters listed on the left of │")
        print("│ the stores                                │")
        print("├───────────────────────────────────────────┤")
        print("│ Type 'settings' or 'options' to access    │")
        print("│ settings which you can change to better   │")
        print("│ suit your playstyle                       │")
        print("├───────────────────────────────────────────┤")
        print("│ Mispelling anything outside of a store    │")
        print("│ results in you losing a life              │")
        print("│ If you lose all your lives, your game is  │")
        print("│ over                                      │")
        print("├───────────────────────────────────────────┤")
        print("│ Type 'time' to show how long you've been  │")
        print("│ playing for                               │")
        print("│ This will also show at the end of the     │")
        print("│ game                                      │")
        print("╘═══════════════════════════════════════════╛")

def GetElapsedTime():
        global startTime

        if (startTime == 0):
                return 0

        elapsedTime = time.time() - startTime
        return round(elapsedTime, 2)

def ClearScreen():
        global clearScreen
        if (clearScreen): print("\x1b[2J")
        

# constant vars
mispellMessages = ["You fool.", "Moron.", "Imbecile.", "Don't let it happen again.", "Clusmy, aren't you?", "Great job, moron.", "Idiot."]
version = "1.1"

# game vars
running = True
startTime = 0

bavis = 0
multiplier = 1
life = 3

totalBavis = 0
totalLives = 3

clearScreen = False

print("╒═══════════════════════════════════════════╕")
print(f"│               BAVIS-RW - {version}v             │")
print("│   https://github.com/QuietAlanB/bavis-rw  │")
print("│       Type 'help' for a basic guide       │")
print("╘═══════════════════════════════════════════╛")

while running:
        text = input("> ")
        ClearScreen()
        
        if (text == "bavis"):
                # start timer
                if (startTime == 0):
                        startTime = time.time()

                bavis += multiplier
                totalBavis += multiplier
                print(f"Bavis: {bavis}")

        elif (text.lower() in ["shop", "store"]):
                Store()

        elif (text.lower() in ["options", "settings", "option", "setting"]):
                Options()

        elif (text.lower() in ["help", "helps", "guide"]):
                HelpText()

        elif (text.lower() in ["time", "gettime", "times"]):
                print(f"Time since start: {GetElapsedTime()} seconds")

        else:
                print(f"{COLOR.RED}{random.choice(mispellMessages)}")
                life -= 1
                print(f"{COLOR.RED}(-1 life, {life} left){COLOR.WHITE}")

                if (life <= 0):
                        time.sleep(2)
                        ClearScreen()
                        print(f"{COLOR.RED}Well done, you lost.{COLOR.WHITE}")
                        running = False

print(f"{COLOR.DARKRED}╒═══════════════════════════════════════════╕")
print(f"{COLOR.DARKRED}│                FINAL STATS                │")
print(f"{COLOR.DARKRED}╘═══════════════════════════════════════════╛")
print(f"{COLOR.RED}Final bavis: {bavis}")
print(f"{COLOR.RED}Multipliers: {multiplier}")
print(f"{COLOR.RED}Total bavis: {totalBavis}")
print(f"{COLOR.RED}Total lives: {totalLives}")
print(f"{COLOR.RED}Total time: {GetElapsedTime()} seconds")
print(f"{COLOR.DARKRED}═════════════════════════════════════════════{COLOR.WHITE}")