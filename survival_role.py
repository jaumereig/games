import sys, os
from PIL import Image
import time
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

# =================
# === FUNCTIONS ===
# =================

# Letters will appear slowly
def print_style(text, color=WHITE, speed = 0.04, end_speed = 0.5, end = True):
    '''
    Color:      color and style of the text
    Speed:      speed of the letters being written
    End_speed:  pause between the end of the writting and the next piece of code
    End:        if True, prints newline. If False, doesn't jump to the next line
    '''
    print(color, end="")
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(speed)
    time.sleep(end_speed)
    if end:
        print(END)

# =============
# === LOBBY ===
# =============
os.system("clear") # Clears the console before starting the game

print_style(DARKCYAN+"Welcome to the ~Bear Grylls Ultimate Survival Skills~ game.")
print_style("Here you will have to pass a series of levels that will challenge your abilities of surviving in the wild with very few resources.")
print_style("Good luck!")
print_style("Please select 3 of the following items to put in your backpack:"+END)
print_style(LIGHTRED+"{}\t{}\t{}\n{}\t{}\t{}\n{}\t{}\t\t\t{}\n".format('- Knife ', '- Stormproof match kit ', '- Flashlight ', '- Bucket ', '- Mosquito repeller ', '- Tent ', '- Sleeping bag ', '- GPS ', '- Water filter bottle'),speed=0.01)
possible_items = ['Knife', 'Stormproof match kit', 'Flashlight', 'Bucket', 'Mosquito repeller', 'Tent', 
    'Sleeping bag', 'GPS', 'Water filter bottle']

backpack = set()

first, second, third = False, False, False

while not first:
    print_style('1) First item:', end_speed=0)
    item1 = input()
    if item1 in possible_items:
        backpack.add(item1)
        first = True
    else:
        print_style("\tERROR! That item doesn't exist or is wrongly written!", speed=0.01)
        print_style("\tTry tipping a valid object as they are written above:", speed=0.01)

while not second:
    print_style('2) Second item:', end_speed=0)
    item2 = input()
    if item2 in possible_items:
        if item2 not in backpack:
            backpack.add(item2)
            second = True
        else:
            print_style("\tThis item is already in your backpack!", speed=0.01)
    else:
        print_style("\tERROR! That item doesn't exist or is wrongly written!", speed=0.01)
        print_style("\tTry tipping a valid object as they are written above:", speed=0.01)


while not third:
    print_style('3) Third item:', end_speed=0)
    item3 = input()
    if item3 in possible_items:
        if item3 not in backpack:
            backpack.add(item3)
            third = True
        else:
            print_style("\tThis item is already in your backpack!", speed=0.01)
    else:
        print_style("\tERROR! That item doesn't exist or is wrongly written!", speed=0.01)
        print_style("\tTry tipping a valid object as they are written above:", speed=0.01)

print_style(DARKCYAN+'Good! You are ready to begin the adventure! This are the items in your backpack to begin with:')

for item in backpack:
    print_style(item+" ", RED, end=False)

print()

print_style(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
print_style(BACKGROUNDBLUE+BLACK+"LEVEL 1"+END+DARKCYAN)
print_style("You are in Manning. This is a valley with poor biodiversity so you have to get out of here and find a place with resources that will ensure your survival.")
print_style(LIGHTRED+"Where do you choose to go?\n{}\n{}\n(Input name only)".format("Cosima -- Land of fairies", "Griffin -- Land of mythological creatures"))
location1 = input()
follow = 0
while follow == 0:
    if location1 =='Cosima' or location1 == 'Griffin':
        follow = True
    else:
        print_style("Where do you choose to go?\n{}\n{}\n(Input name only)".format("Cosima -- Land of fairies", "Griffin -- Land of mythological creatures"))
        location1 = input()

if location1 == 'Cosima':
    print_style(DARKCYAN+"Good choice!\nAfter a few days walking you seem to have found a nice green grassland. You walk around and discover a huge diversity of fruits and plants that you have never seen before.")
    print_style('There is even a river with crystalline water. You deserve drinking so you stop for a bit and enjoy yourself.')
    a = """Hey! Wake up! You fell asleep. It is time to get up and keep discovering what's new. Oh, wait. Something looks wrong. You got some rashes on your arms.
    It must have been the water you just had. Luckily, in BIO 101 professor Layton once talked about this fruit that can ease skin rushes. You can't remember 
    the name but you do remember that the fruit was red and triangular."""
    print_style(a)
    LIFE_POINTS = LIFE_POINTS - 500
    print_style(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
    print_style(LIGHTRED+'Where will you go?\n{}\n{}\n(Input capital letter only)'.format("A - Away from the river", 'B - Cross the river '))
    direction1 = input()
    follow = 0
    while follow == 0:
        if direction1 == 'A' or direction1 == 'B':
            follow = True
        else:
            print_style("Where will you go?\n{}\n{}\n(Input capital letter only)".format("A - Away from the river", 'B - Cross the river '))
            direction1 = input()

    if direction1 == 'A':
        a = """You are going towards a yet to be discovered land. Is there going to be the fruit that you need to relieve your pain? We shall discover!
        After walking through a plain with essentially low grass plants you see taller trees towards the horizon.
        Running is your best choice... You have reached the tall trees."""
        b = """ Bingo! These trees have fruits. Now is time for you to find the red and triangular fruit that professor Layton mentioned in class. There
        is one tree with a similar fruit. You take a few and eat one carefully.
         """
        print_style(DARKCYAN+a+b)
        LIFE_POINTS = LIFE_POINTS + 200
        print_style(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
        a = """Now that you have recovered you keep walking around the trees and recollect some fruits. This particular tree is drawing your attention.
        The crown of the tree is emitting a neon green light all around it. Get closer and discover what is going on!
        There are small creatures flying around the tree! They are tiny and move very fast, have little wings which are actually emitting the neon
        green light. If you move your hands towards them... they actually come closer to you. Maybe they actually like you and you are being welcomed.
        (Fairy)- Hello visitor! My name is Acantha. What is your name?"""
        print_style(DARKCYAN+a)
        player_name = input() # Introduction of player and variable can be used all along the program
        """ Here there is some error """
        a ="""(Acantha)- Nice to meet you """
        b = """, I must warn you that it is not safe for you to stay here. At mid night the creatures from the underground arise and become deadly
        carnivores which will not leave any trace of life behind them. However, I am afraid there is no time left for you to leave so we shall provide
        you with our hideout to keep you protected."""
        print_style(a+player_name+b)
        a="""- Okay. Hold on. I can't believe this is real! You look like a tiny human the size of my pinky and you can speak like me, that is so cool!
        Though, I am very interested in knowing more about these underground animals you are talking about. How can I know they won't hurt me?
        (Acantha)- You haven't seen any of us but we have seen many of you instead. The creatures I am talking about are gigantic, they live underground
        and can see at night everything around them, just like you do during the day. They even have the capacity to perceive the temperature of their 
        surroundings them. This is how they identify bigger prays while they are sleeping. We call them Minotaurus. Trust me they are pure evil.
        So that you can survive you will need an invisibility cloak. I can offer you one but first you must help me."""
        print_style("({}){}".format(player_name,a))
        a="""-Of course. I have no choice, and I really want to have that invisibility cloack. How can I help you?
        (Acantha)- I need you to solve a puzzle. Unfortunately, a witch enchanted our tree and it is dying. We can only unlock the enchantment by writing
        the correct code number onto the base of the tree's trunk. All we know is that the code is 3 digits long and we only have 3 tries left. Can you help?"""
        print_style("({}){}\nWrite y if you are ready to solve the puzzle.".format(player_name,a))
        confirmation = input()
        follow = 0
        while follow == 0:
            if confirmation == 'YES' or confirmation == 'yes' or confirmation == 'y':
                follow = True
            else:
                print_style("Write y if you are ready to solve the puzzle.")
                confirmation = input()
        a="""-I will try. Let me see the puzzle."""
        print_style("({}){}".format(player_name,a))
        image = Image.open('A_cosima1.png')
        # image.show() 
        cosima_puzzle = input()
        print_style("({})- My answer code to unlock the enchantment is: {}.".format(player_name, cosima_puzzle))
        follow = 0
        tries_left = 3
        while follow == 0 and tries_left >= 2:
            if cosima_puzzle == '153':
                print_style("Correct answer")
                follow = 1
            else:
                tries_left -= 1
                print_style("The code is incorrect. Try again! Tries left: {}".format(tries_left))
                cosima_puzzle = input()
                LIFE_POINTS = LIFE_POINTS - 500 # Every miss takes 500 LP away
        if tries_left <= 1:
            print_style("You lost all your opportunities.")
            print_style(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
            sys.exit(0) # this if we want to finish game when player fails to pass a test
        else:
            print_style(player_name+", you are successful!")
            print_style(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
            a="""(Acantha)- Fantastic! The code works. This is going to break the enchantment which means that we will stay in our home. We
            appreciate your effort. As promised, we are giving you the invisibility cloak as a reward."""
            print_style(DARKCYAN+"{}".format(a))
            print_style(LIGHTRED+'Backpack:'+END)
            backpack.add('Invisibility cloak')
            for i in backpack:
                print_style(LIGHTRED+i+END)
        a = """Now is getting dark. As Acantha told you the minotaurus will appear soon and scavenge all around the area. They are starving. 
        Fortunately, you can use the invisibility cloak while you spend the night under the tree from Acantha. You have succesfully passed the first
        enigma and in the morning you will travel to your next location. Move on!"""
        #print_style(DARKCYAN+"{}".format(LIFE_POINTS))
    if direction1 == 'B':
        LIFE_POINTS = LIFE_POINTS - 500
        a = """ You are crossing the river and thus water is in contact with you. You are hurrying to get to the other side because water seems to be
        slightly poisonous.  On the other side of the river the landscape is just the same. However, it smells somewhat different. You shall trace 
        that smell and find out where it comes from!"""
        print_style(DARKCYAN+a)
        print_style(BOLD+'LIFE POINTS: {}.'.format(LIFE_POINTS)+END)
        a = """The smell is definitely coming from this tree in front of you right now.  """

# print_style(BACKGROUNDBLUE+BLACK+"LEVEL 2"+END+DARKCYAN)

else:
    print_style("Great choice!", color=DARKCYAN)
    print_style("")
