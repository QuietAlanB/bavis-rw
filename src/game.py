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
        global bavis
        global life
        
        maxMultCost = int(bavis - bavis % 50)
        if (bavis < 50):
                maxMultCost = 50

        lifeCost = 35 ** (life + 1)

        # text
        oneMultText = f"{COLOR.GREEN}50b{COLOR.WHITE}"
        maxMultText = f"{COLOR.GREEN}{maxMultCost}b{COLOR.WHITE}"
        userMultText = f"{COLOR.GREEN}50b each{COLOR.WHITE}"
        lifeCostText = f"{COLOR.GREEN}{lifeCost}b{COLOR.WHITE}"
        if (bavis < 50):
                oneMultText = f"{COLOR.RED}50b{COLOR.WHITE}"
                maxMultText = f"{COLOR.RED}{DisplayNumber(maxMultCost)}b{COLOR.WHITE}"
                userMultText = f"{COLOR.RED}50b each{COLOR.WHITE}"

        if (bavis < lifeCost):
                lifeCostText = f"{COLOR.RED}{DisplayNumber(lifeCost)}b{COLOR.WHITE}"

        print("╒═══════════════════════════════════════════╕")
        print("│                BAVIS STORE                │")
        print("├───────────────────────────────────────────┤")
        print("│        (Type the number/letter of         │")
        print("│           what you'd like to do)          │")
        print("╞═══════════════ MULTIPLIERS ════╤══════════╛")
        print(f"│ 1. 1x Multiplier               │ {oneMultText}")
        print(f"│ 2. Max Multipliers             │ {maxMultText}")
        print(f"│ 3. User specified multipliers  │ {userMultText}")
        print("╞═══════════════════ LIVES ══════╪═══════════")
        print(f"│ 4. +1 life                     │ {lifeCostText}")
        print("╘════════════════════════════════╧═══════════")

        text = input("[BAVIS STORE] > ")
        ClearScreen()

        if (text == "1" or text == "1."): BuyMultiplier(0)
        if (text == "2" or text == "2."): BuyMultiplier(1)
        if (text == "3" or text == "3."): BuyMultiplier(2)
        
        if (text == "4" or text == "4."): BuyLife()

# options
def Options():
        global clearScreen
        global commaNumber

        print("╒═══════════════════════════════════════════╕")
        print("│          BAVIS SIMULATOR OPTIONS          │")
        print("├───────────────────────────────────────────┤")
        print("│        (Type the number/letter of         │")
        print("│         what you'd like to change)        │")
        print("╞═══════════════════════════════════════════╡")
        if (clearScreen): print(f"│ {COLOR.GREEN}1. Clear screen after input            ON {COLOR.WHITE}│")
        else: print(f"│ {COLOR.RED}1. Clear screen after input           OFF {COLOR.WHITE}│")
        if (commaNumber): print(f"│ {COLOR.GREEN}2. Display numbers with commas         ON {COLOR.WHITE}│")
        else: print(f"│ {COLOR.RED}2. Display numbers with commas        OFF {COLOR.WHITE}│")
        print("╘═══════════════════════════════════════════╛")

        text = input("[OPTIONS] > ")
        ClearScreen()

        if (text == "1" or text == "1."): 
                clearScreen = not clearScreen
                if (clearScreen): print(f"{COLOR.GREEN}[-] Turned on screen clear{COLOR.WHITE}")
                else: print(f"{COLOR.RED}[-] Turned off screen clear{COLOR.WHITE}")

        if (text == "2" or text == "2."): 
                commaNumber = not commaNumber
                if (commaNumber): print(f"{COLOR.GREEN}[-] Turned on commas in numbers{COLOR.WHITE}")
                else: print(f"{COLOR.RED}[-] Turned off commas in numbers{COLOR.WHITE}")


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

        print(f"{DisplayNumber(multBought)} multiplier(s) bought! ({DisplayNumber(multiplier)} now)")

def BuyLife():
        global bavis
        global life
        global totalBoughtLives
        
        cost = 35 ** (life + 1)

        if (bavis < cost):
                print(f"[!] You don't have enough bavis!")
                return

        bavis -= cost
        life += 1
        totalBoughtLives += 1
        print(f"+1 life ({life} now)")
        
def HelpText():
        print("╒═══════════════════════════════════════════╕")
        print("│            BAVIS SIMULATOR HELP           │")
        print("├─────────────── HOW TO PLAY ───────────────┤")
        print("│ Type 'bavis' to increase your bavis by 1. │")
        print("│ Using 'bavis' is how you play the game.   │")
        print("│ There are many 'areas' you can go to that │")
        print("│ you can buy stuff from, do stuff at, and  │")
        print("│ so on - These will help you progress.     │")
        print("│ Mispelling anything outside of an area    │")
        print("│ results in you losing a life.             │")
        print("│ If you lose all your lives, your game is  │")
        print("│ over.                                     │")
        print("├─────────────── AREAS - SHOP ──────────────┤")
        print("│ Type 'shop' or 'store' to access the      │")
        print("│ shop.                                     │")
        print("│ This shop allows you to access the        │")
        print("│ bavis store and the golden store.         │")
        print("│ You can buy various items for bavis from  │")
        print("│ the bavis store, such as multipliers,     │")
        print("│ lives, and so on.                         │")
        print("│ The golden store sells items for golden   │")
        print("│ bavis, such as bavis, crates, boosters,   │")
        print("│ badges and so on.                         │")
        print("├───────────────── COMMANDS ────────────────┤")
        print("│ Type 'settings' or 'options' to access    │")
        print("│ settings which you can change to better   │")
        print("│ suit your style.                          │")
        print("│                                           │")
        print("│ Type 'time' to show the amount of time    │")
        print("│ elapsed since you started the game.       │")
        print("│                                           │")
        print("│ Type 'stats' or 'stat' to show your       │")
        print("│ current statistics.                       │")
        print("│                                           │")
        print("│ Type 'finish' or 'done' to instantly end  │")
        print("│ the game and display statistics.          │")
        print("╘═══════════════════════════════════════════╛")

def GetElapsedTime():
        if (startTime == 0):
                return 0

        elapsedTime = time.time() - startTime
        return round(elapsedTime, 2)

# returns time as a string in minutes:seconds.millisecond format
def DisplayTime():
        seconds = GetElapsedTime()
        minutes = int(seconds // 60)
        seconds = round(seconds % 60, 2)

        secondsString = str(seconds)
        minutesString = str(minutes)

        if (len(str(int(seconds))) <= 1):
                secondsString = "0" + secondsString

        if (len(minutesString) <= 1):
                minutesString = "0" + minutesString
        
        return f"{minutesString}:{secondsString}"

def ShowStats():
        print(f"╒═══════════════════════════════════════════╕")
        print(f"│                 STATISTICS                │")
        print(f"├───────────────────────────────────────────┘")
        print(f"│ Bavis: {DisplayNumber(bavis)}")
        print(f"│ Multipliers: {DisplayNumber(multiplier)}")
        print(f"│ Total bavis collected: {DisplayNumber(totalBavis)}")
        print(f"│ Total lives bought: {DisplayNumber(totalBoughtLives)}")
        print(f"│ Total lives lost: {DisplayNumber(totalLostLives)}")
        print(f"│ Total time: {DisplayTime()}")
        print(f"│ Version: v{version}")
        print(f"╘═══════════════════════════════════════════")

# can be toggled in options
def ClearScreen():
        if (clearScreen): print("\x1b[2J")

# converts numbers to strings with commas in between every 3 digits (e.g 55555 -> 55,555)
# can be toggled in options
def DisplayNumber(n):
        if (not commaNumber):
                return str(n)

        numString = str(n)
        string = ""
        digitRemainder = len(numString) % 3

        if (digitRemainder == 0):
                digitRemainder = 3

        placeCommaVar = digitRemainder - 1

        for i in range(len(numString)):
                string += numString[i]
                if (placeCommaVar == 0 and i != len(numString) - 1):
                        string += ","
                        placeCommaVar = 3

                placeCommaVar -= 1

        return string

# constant vars
mispellMessages = ["You fool.", "Moron.", "Imbecile.", "Don't let it happen again.", "Clusmy, aren't you?", "Great job, moron.", "Idiot."]
version = "1.2"

# game vars
running = True
startTime = 0

bavis = 0
multiplier = 1
life = 3

totalBavis = 0
totalBoughtLives = 0
totalLostLives = 0

clearScreen = False
commaNumber = True

print("╒═══════════════════════════════════════════╕")
print(f"│               BAVIS-RW - v{version}             │")
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
                print(f"Bavis: {DisplayNumber(bavis)}")

        elif (text.lower() in ["options", "settings", "option", "setting"]):
                Options()

        elif (text.lower() in ["help", "helps", "guide"]):
                HelpText()

        elif (startTime == 0):
                print("GAME NOT STARTED - Type 'bavis' to start the game")
                pass

        elif (text.lower() in ["shop", "store"]):
                Store()

        elif (text.lower() in ["time", "gettime", "times"]):
                print(f"Time since start: {DisplayTime()}")
        
        elif (text.lower() in ["stats", "stat", "statistics", "statistic"]):
                ShowStats()

        elif (text.lower() in ["end", "done", "finish"]):
                print(f"{COLOR.RED}Game ended, well done.{COLOR.WHITE}")
                break

        else:
                life -= 1
                totalLostLives += 1

                print(f"{COLOR.RED}{random.choice(mispellMessages)}")
                print(f"{COLOR.RED}(-1 life, {life} left){COLOR.WHITE}")

                if (life <= 0):
                        time.sleep(2)
                        ClearScreen()
                        print(f"{COLOR.RED}Well done, you lost.{COLOR.WHITE}")
                        running = False

print(COLOR.DARKRED)
ShowStats()
print(COLOR.WHITE)

input("Press ENTER to quit...")