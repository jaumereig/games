import sys
from PIL import Image
"""
image = Image.open('Image1.png')
image.show() 
easy code for showing images in current directory (png or jpg format)
"""
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
    a = """Hey! Wake up! You fell asleep. It is time to get up and keep discovering what's new. Oh, wait. Something looks wrong. You got some rashes on your arms.
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
        a = """You are going towards a yet to be discovered land. Is there going to be the fruit that you need to relieve your pain? We shall discover!
        After walking through a plain with essentially low grass plants you see taller trees towards the horizon.
        Running is your best choice... You have reached the tall trees."""
        b = """ Bingo! These trees have fruits. Now is time for you to find the red and triangular fruit that professor Layton mentioned in class. There
        is one tree with a similar fruit. You take a few and eat one carefully.
         """
        print(DARKCYAN+a+b)
        LIFE_POINTS = LIFE_POINTS + 200
        print(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
        a = """Now that you have recovered you keep walking around the trees and recollect some fruits. This particular tree is drawing your attention.
        The crown of the tree is emitting a neon green light all around it. Get closer and discover what is going on!
        There are small creatures flying around the tree! They are tiny and move very fast, have little wings which are actually emitting the neon
        green light. If you move your hands towards them... they actually come closer to you. Maybe they actually like you and you are being welcomed.
        (Fairy)- Hello visitor! My name is Acantha. What is your name?"""
        print(DARKCYAN+a)
        player_name = input() # Introduction of player and variable can be used all along the program
        a ="""(Acantha)- Nice to meet you """
        b = """, I must warn you that it is not safe for you to stay here. At mid night the creatures from the underground arise and become deadly
        carnivores which will not leave any trace of life behind them. However, I am afraid there is no time left for you to leave so we shall provide
        you with our hideout to keep you protected."""
        print(a+player_name+b)
        a="""- Okay. Hold on. I can't believe this is real! You look like a tiny human the size of my pinky and you can speak like me, that is so cool!
        Though, I am very interested in knowing more about these underground animals you are talking about. How can I know they won't hurt me?
        (Acantha)- You haven't seen any of us but we have seen many of you instead. The creatures I am talking about are gigantic, they live underground
        and can see at night everything around them, just like you do during the day. They even have the capacity to perceive the temperature of the bodies
        surrounding them. This is how they identify bigger prays while they are sleeping. We call them Minotaurus. Trust me they are pure evil.
        So that you can survive you will need an invisibility cloak. I can offer you one but first you must help me."""
        print("({}){}".format(player_name,a))
        a="""-Of course. I have no choice, and I really want to have that invisibility cloack. How can I help you?
        (Acantha)- I need you to solve a puzzle. Unfortunately, a witch enchanted our tree and it is dying. We can only unlock the enchantment by writing
        the correct code number onto the base of the tree's trunk. All we know is that the code is 3 digits long and we only have 3 tries left. Can you help?"""
        print("({}){}\nWrite y if you are ready to solve the puzzle.".format(player_name,a))
        confirmation = input()
        follow = 0
        while follow == 0:
            if confirmation == 'YES' or confirmation == 'yes' or confirmation == 'y':
                follow = True
            else:
                print("Write y if you are ready to solve the puzzle.")
                confirmation = input()
        a="""-I will try. Let me see the puzzle."""
        print("({}){}".format(player_name,a))
        image = Image.open('A_cosima1.png')
        image.show() 
        cosima_puzzle = input()
        print("({})- My answer code to unlock the enchantment is: {}.".format(player_name, cosima_puzzle))
        follow = 0
        tries_left = 3
        while follow == 0 and tries_left >= 2:
            if cosima_puzzle == '153':
                print("Correct answer")
                follow = 1
            else:
                tries_left -= 1
                print("The code is incorrect. Try again! Tries left: {}".format(tries_left))
                cosima_puzzle = input()
        LIFE_POINTS = LIFE_POINTS - 1000
        if tries_left <= 1:
            print("You lost all your opportunities.")
            print(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
            sys.exit(0) # this if we want to finish game when player fails to pass a test
        else:
            print("You are successful!")
            a="""(Acantha)- Fantastic! The code works. This is going to break the enchantment which means that we will stay in our home. We
            appreciate your effort. As promised, we are giving you the invisibility cloak as a reward."""
            print("{}".format(a))
            print(LIGHTRED+'Backpack:'+END)
            backpack.append('Invisibility cloak')
            for i in backpack:
                print(LIGHTRED+i+END)
        print("continues here")
    if direction1 == 'B':
        LIFE_POINTS = LIFE_POINTS - 500
        a = """ You are crossing the river and thus water is in contact with you. You are hurrying to get to the other side because water seems to be
        slightly poisonous.  On the other side of the river the landscape is just the same. However, it smells somewhat different. You shall trace 
        that smell and find out where it comes from!"""
        print(DARKCYAN+a)
        print(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
        a = """The smell is definitely coming from this tree in front of you right now.  """
