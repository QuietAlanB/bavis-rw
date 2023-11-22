import random
import os
import time
from color import COLOR

os.system("")

# functions for menus
def Shop():
        print("================== STORE ==================")
        print("(Type the letter/number of what you'd like)")
        print("")
        print("---------------- Quick buy ----------------")
        print("a. Max multipliers")
        print("")
        print("------------------ Shops ------------------")
        print("1. Upgrades")
        print("2. Special items")
        print("")
        print("x. Leave store")

        text = input("[SHOP] > ")
        ClearLines()
        if (text == "a" or text == "a."): BuyMultipliers(2)
        if (text == "1" or text == "1."): UpgradesShop()
        if (text == "2" or text == "2."): SpecialShop()

        if (text == "x" or text == "x."): return

def UpgradesShop():
        print("================= UPGRADES ================")
        print("(Type the letter/number of what you'd like)")
        print("")
        print("--------------- Multipliers ---------------")
        print("     (Multipliers grant you more bavis)    ")
        print("1. +1 Multiplier                       (50)")
        print("2. Custom amount of multipliers")
        print("3. Max amount of multipliers")
        print("")
        print("------------------ Lives ------------------")
        print("  (Lives increase in price exponentially)  ")
        print("4. +1 Life")
        print("")
        print("x. Leave store")
        print("z. Go back to previous store")

        text = input("[UPGRADES] > ")
        ClearLines()
        if (text == "1" or text == "1."): BuyMultipliers(0)
        if (text == "2" or text == "2."): BuyMultipliers(1)
        if (text == "3" or text == "3."): BuyMultipliers(2)

        if (text == "4" or text == "4."): BuyLife()
        
        if (text == "x" or text == "x."): return
        if (text == "z" or text == "z."): Shop()

def SpecialShop():
        print("============== SPECIAL ITEMS ==============")
        print("(Type the letter/number of what you'd like)")
        print("")
        print("----------------- Goldens -----------------")
        print(f"    ({COLOR.YELLOW}Golden bavis{COLOR.WHITE} are rare drops from    ")
        print("               regular bavis)             ")
        print("1. Turn golden bavis into regular bavis")
        print("2. Golden Crates")
        print("3. Boosters")
        print("4. Badge")
        print("")
        print("x. Leave store")
        print("z. Go back to previous store")

        text = input("[SPECIAL SHOP] > ")
        ClearLines()

def BuyMultipliers(type):
        global bavis
        global multiplier

        if (type == 0): 
                if (bavis < 50):
                        print(f"You don't have enough bavis!")
                        return
                
                bavis -= 50
                multiplier += 1
                print(f"1 Multiplier bought! ({multiplier} now)")

        elif (type == 1):
                print("How many multipliers would you like?")
                multipliers = input("[MULTIPLIERS] > ")
                ClearLines()
                # error handling
                try: 
                        multipliers = int(multipliers)
                        if (multipliers < 1):
                                print("Why...?")
                                return
                        cost = multipliers * 50
                        if (bavis >= cost):
                                bavis -= cost
                                multiplier += multipliers
                                print(f"{multipliers} Multiplier(s) bought! ({multiplier} now)")
                        else:
                                print(f"You don't have enough bavis!")
                except:
                        print("[ERROR] Not a number")

        elif (type == 2):
                if (bavis < 50):
                        print(f"You don't have enough bavis!")
                        return
                
                remainder = bavis % 50
                multipliers = int((bavis - remainder) / 50)
                cost = multipliers * 50
                bavis -= cost
                multiplier += multipliers
                print(f"{multipliers} Multiplier(s) bought! ({multiplier} now)")

def BuyLife():
        global bavis
        global life

        cost = 35 ** (life + 1)
        print(f"Buying another life will cost {cost} bavis\nAre you sure you would like to buy this? (y/n)")
        text = input("[LIVES] > ")
        ClearLines()

        if (bavis < cost):
                print(f"You don't have enough bavis!")
                return
        
        if (text in ["y", "Y", "yes", "YES"]):
                bavis -= cost
                life += 1
                print(f"1 More life bought! ({life} now)")

        elif (text in ["n", "N", "no", "NO"]):
                return
        
def ConvertGoldenBavis():
        global bavis
        value = goldenChance * multiplier

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
goldenBavis = 0
crystalBavis = 0
goldenChance = 10000
crystalChance = 1000

clearLines = False

# game
while running:
        text = input("> ")
        ClearLines()
        
        if (text == "bavis"):
                bavis += 1 * multiplier
                print(f"Bavis: {bavis}")

                if (random.randint(1, goldenChance)) == 1:
                        goldenBavis += 1
                        print(f"{COLOR.YELLOW}!! You just got a GOLDEN BAVIS !!{COLOR.WHITE}")

                if (random.randint(1, crystalChance) == 1):
                        crystalBavis += 1
                        print(f"{COLOR.PURPLE}!?! You just got a CRYSTAL BAVIS !?!{COLOR.WHITE}")

        elif (text == "shop"):
                Shop()

        else:
                life -= 1
                print(f"{COLOR.DARKRED}{random.choice(mispellMessages)}")
                print(f"-1 Life ({life} left){COLOR.WHITE}")

                # end
                if (life <= 0):
                        time.sleep(2)
                        running = False
                        print(f"{COLOR.DARKRED}Game over.{COLOR.WHITE}")
                        time.sleep(2)