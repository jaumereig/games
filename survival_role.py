
""" import sys """
# My update "Tres tristes tigres comen trigo de un trigal" "Jamba part II"

# =======================
# === START VARIABLES ===
# =======================

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
BLACK = "\033[30m"
LIGHTGRAY = "\033[37m"
DARKGRAY = "\033[90m"
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
LIGHTRED = "\033[91m"
WHITE = "\033[97m"
BOLD = '\033[1m'
BACKGROUNDWHITE = "\033[107m"
BACKGROUNDDEFAULT      = "\033[49m"
BACKGROUNDBLACK      = "\033[40m"
BACKGROUNDRED        = "\033[41m"
BACKGROUNDGREEN        = "\033[42m"
BACKGROUNDYELLOW       = "\033[43m"
BACKGROUNDBLUE     = "\033[44m"
RESETBOLD = "\033[21m"
UNDERLINE = '\033[4m'
DIM = "\033[2m"
BLINK = "\033[5m"
REVERSE = "\033[7m"
HIDDEN = "\033[8m"
DEFAULT = "\033[39m"
END = '\033[0m'

LIFE_POINTS = 10000


# =============
# === LOBBY ===
# =============

print(DARKCYAN+"Welcome to the Bear Grylls Ultimate Survival Skills game.\nHere you will have to pass a series of levels that will challenge your abilities of surviving in the wild with very few resources.\nGood luck!")
print("Please select 3 of the following items to put in your backpack:"+END)
print(LIGHTRED+"{}\t{}\t{}\n{}\t{}\t{}\n{}\t{}\t{}\n".format('Knife', 'Stormproof match kit', 'Flashlight', 'Bucket', 'Mosquito repeller', 'Tent', 
    'Sleeping bag', 'GPS', 'Water filter bottle'))
possible_items = ['Knife', 'Stormproof match kit', 'Flashlight', 'Bucket', 'Mosquito repeller', 'Tent', 
    'Sleeping bag', 'GPS', 'Water filter bottle']

print('First item:')
item1 = input()
print('Second item:')
item2 = input()
print('Third item:')
item3 = input()

backpack = []
if item1 in possible_items:
    backpack.append(item1)
if item2 in possible_items:
    backpack.append(item2)
if item3 in possible_items:
    backpack.append(item3)
ready_to_start = 0
while ready_to_start == False:
    if len(backpack) == 3:
        print(DARKCYAN+'Good! You are ready to begin the adventure! This are the items in your backpack to begin with:')
        for i in backpack:
            print(i)
        ready_to_start = 1
    else:
        print('Looks like you have not filled your backpack with the required number of items. Remember to select 3 and write them as they appear in the menu.')
        for i in range(3-len(backpack)):
            print('Add item:')
            newitem = input()
            if newitem in possible_items:
                backpack.append(newitem)
                if len(backpack) == 3:
                    print('Good! You are ready to begin the adventure! This are the items in your backpack to begin with:')
                    for i in backpack:
                        print(i)
                    ready_to_start = 1
print(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
print(BACKGROUNDBLUE+BLACK+"LEVEL1"+END+DARKCYAN)
print("You are in Manning. This is a valley with poor biodiversity so you have to get out of here and find a place with resources that will ensure your survival.")
print(LIGHTRED+"Where do you choose to go?\n{}\n{}\n(Input name only)".format("Cosima -- Land of fairies", "Griffin -- Land of mythological creatures"))
location1 = input()
follow = 0
while follow == 0:
    if location1 =='Cosima' or location1 == 'Griffin':
        follow = True
    else:
        print("Where do you choose to go?\n{}\n{}\n(Input name only)".format("Cosima -- Land of fairies", "Griffin -- Land of mythological creatures"))
        location1 = input()

if location1 == 'Cosima':
    print(DARKCYAN+"Good choice!\nAfter a few days walking you seem to have found a nice green grassland. You walk around and discover a huge diversity of fruits and plants that you have never seen before.")
    print('There is even a river with crystalline water. You deserve drinking so you stop for a bit and enjoy yourself.')
    a = """
    Hey! Wake up! You fell asleep. It is time to get up and keep discovering what's new. Oh, wait. Something looks wrong. You got some rashes on your arms.
    It must have been the water you just had. Luckily, in BIO 101 professor Layton once talked about this fruit that can ease skin rushes. You can't remember 
    the name but you do remember that the fruit was red and triangular."""
    print(a)
    LIFE_POINTS = LIFE_POINTS - 500
    print(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
    print(LIGHTRED+'Where will you go?\n{}\n{}\n(Input capital letter only)'.format("A - Away from the river", 'B - Cross the river '))
    direction1 = input()
    follow = 0
    while follow == 0:
        if direction1 == 'A' or direction1 == 'B':
            follow = True
        else:
            print("Where will you go?\n{}\n{}\n(Input capital letter only)".format("A - Away from the river", 'B - Cross the river '))
            direction1 = input()

    if direction1 == 'A':
        a = """
        You are going towards a yet to be discovered land. Is there going to be the fruit that you need to relieve your pain? We shall discover!
        After walking through a plain with essentially low grass plants you see taller trees towards the horizon.
        Running is your best choice... You have reached the tall trees."""
        b = """ 
        Bingo! These trees have fruits. Now is time for you to find the red and triangular fruit that professor Layton mentioned in class. There
        is one tree with a similar fruit. You take a few and eat one carefully.
         """
        print(DARKCYAN+a+b)
        LIFE_POINTS = LIFE_POINTS + 200
        print(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
        """ introduce fairies """
    if direction1 == 'B':
        LIFE_POINTS = LIFE_POINTS - 500
        a = """ 
        You are crossing the river and thus water is in contact with you. You are hurrying to get to the other side because water seems to be
        slightly poisonous.  On the other side of the river the landscape is just the same. However, it smells somewhat different. You shall trace 
        that smell and find out where it comes from!"""
        print(DARKCYAN+a)
        print(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
        a = """ 
        The smell is definitely coming from this tree in front of you right now.  """

