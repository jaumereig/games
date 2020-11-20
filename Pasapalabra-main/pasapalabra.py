import sys, pygame, os, random, math, time

pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()


# =================
# === VARIABLES ===
# =================
screen_width, screen_height = 1320, 700
pausa = True        # True: time will be passing | False: Time is frozen
game_end = False    # True: Game has ended | False: Game is still going
winner = None       # None: No winner | Possible options: Player1 or Player2

music = False       # True: Music will play | False: Music won't play
volume = 0.5

CT = 60             # Clock tick (needed for pygame velocity)
start_ticks = pygame.time.get_ticks()   # Current miliseconds (needed to compute seconds)

screen = pygame.display.set_mode((screen_width, screen_height)) # Create screen

abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

rosco_width, rosco_height = 700, 700
rosco_x, rosco_y = screen_width/4-20, 3     # Coordinates of rosco on the screen

letter_width, letter_height=69, 69
radius_letter = letter_width/2

pasapalabra_width, pasapalabra_height = 300, 150
pasapalabra_x, pasapalabra_y = 50, 550      # Coordinates of pasapalabra text on the screen

score_rectangle_width, score_rectangle_height = 250, 400
score_rectangle_x, score_rectangle_y = 75, 200      # Coordinates of time rectangle on the screen

button_state = 0    # 0: Button not pressed | 1: Burron pressed

max_time = 15       # Total time per question/letter
time_spent = 0      # Time spent from the total time

# ==============
# === COLORS ===
# ==============
black = 0,0,0
white = 255, 255, 255
orange = 255, 140, 0


# ====================
# === FONTS & TEXT ===      # Loading and render of all texts and fonts
# ====================
pasapalabra_font = pygame.font.Font("Fonts/Golden_Metafor_Regular.ttf", 30)
pasapalabra_text = pasapalabra_font.render("Pasapalabra", False, white)

time_font = pygame.font.Font("Fonts/MEDIO_VINTAGE.otf", 50)
time_text = time_font.render("TIEMPO", False, white)

empate_font = pygame.font.Font("Fonts/MEDIO_VINTAGE.otf", 100)
empate_text = empate_font.render("Empate", False, orange)

time_font_75 = pygame.font.Font("Fonts/MEDIO_VINTAGE.otf", 75)


# ===================
# === MUSIC & SFX ===       # Loading of music and sfx
# ===================
pygame.mixer.music.load("Sounds/Layton_puzzle_theme.mp3")
pygame.mixer.music.set_volume(volume)

correct_sfx = pygame.mixer.Sound("Sounds/correct.wav")
wrong_sfx = pygame.mixer.Sound("Sounds/wrong.wav")
pygame.mixer.Sound(correct_sfx).set_volume(volume)
pygame.mixer.Sound(wrong_sfx).set_volume(volume)

# ==============
# === IMAGES ===            # Loading of images
# ==============
fondo_azul = pygame.transform.scale( pygame.image.load('Images/fondo_azul_2.jpg'),   (screen_width, screen_height))

unpressed_blue_button = pygame.transform.scale( pygame.image.load('Images/blue_button.png'), (pasapalabra_width, pasapalabra_height))
pressed_blue_button = pygame.transform.scale( pygame.image.load('Images/pressed_blue_button.png'), (pasapalabra_width, pasapalabra_height))
unpressed_orange_button = pygame.transform.scale( pygame.image.load('Images/orange_button.png'), (pasapalabra_width, pasapalabra_height))
pressed_orange_button = pygame.transform.scale( pygame.image.load('Images/pressed_orange_button.png'), (pasapalabra_width, pasapalabra_height))

rosco_azul = pygame.transform.scale( pygame.image.load('Images/rosco_azul.png'),   (rosco_width, rosco_height))

blue_rectangle = pygame.transform.scale( pygame.image.load('Images/blue_rectangle.png'),   (score_rectangle_width, score_rectangle_height))
orange_rectangle = pygame.transform.scale( pygame.image.load('Images/orange_rectangle.png'),   (score_rectangle_width, score_rectangle_height))
red_rectangle = pygame.transform.scale( pygame.image.load('Images/red_rectangle.png'),   (score_rectangle_width, score_rectangle_height))

Player1_image = pygame.transform.scale( pygame.image.load(sys.argv[1]), (350, 350))
Player2_image = pygame.transform.scale( pygame.image.load(sys.argv[2]), (350, 350))

verde_letter2image = {}     # Dictionary relating each letter with its green image path
rojo_letter2image  = {}     # Dictionary relating each letter with its red image path
for letter in abecedario:
    verde_letter2image["verde_{}".format(letter)] = pygame.transform.scale(pygame.image.load("Images/Verde/verde_{}.png".format(letter)), (letter_width, letter_height))
    rojo_letter2image["rojo_{}".format(letter)] = pygame.transform.scale(pygame.image.load("Images/Rojo/rojo_{}.png".format(letter)),(letter_width, letter_height))

congratulations = pygame.transform.scale( pygame.image.load('Images/congratulations.png'), (screen_width//2, screen_height//3))

# Coordinates on the screen of each letter (x pixels, y pixels) ("x" starts from the LEFT of the screen and "y" starts from the TOP of the screen)
letter2coord = {
    "A": (621,2),
    "B": (690,10),
    "C": (758,30),
    "D": (820,70),
    "E": (870,120),
    "F": (910,185),
    "G": (932,253),
    "H": (940,325),
    "I": (930,396),
    "J": (903,462),
    "K": (865,520),
    "L": (815,570),
    "M": (755,605),
    "N": (690,625),
    "Ñ": (619,630),
    "O": (547,620),
    "P": (477,595),
    "Q": (412,550),
    "R": (365,495),
    "S": (330,429),
    "T": (310,358),
    "U": (312,285),
    "V": (327,210),
    "W": (363,145),
    "X": (413,80),
    "Y": (477,35),
    "Z": (547,10),
    
}

# ===============
# === CLASSES ===
# ===============

class Player:
    def __init__(self, image):
        self.letters2state = {}                     # Dictionary relating each letter to its state (0, 1 or 2)
        for letter in abecedario:
            self.letters2state[letter] = 1          # 0: not answered | 1: Verde | 2: Rojo
        
        self.rectangle = blue_rectangle                 # Time rectangle
        self.unpressed_button = unpressed_blue_button
        self.pressed_button = pressed_blue_button
        
        self.fondo = fondo_azul     # Background image
        self.rosco = rosco_azul     # Rosco image
        self.image = image          # Center image
        self.end = False            # True: player has completed all letters | False: player hasn't completed all letters
        self.is_Any0 = True         # True: there are letters in blue| False: there are no letters in blue (all either green or red)
        


# ==============
# === PLAYER ===
# ==============

Player1, Player2 = Player(Player1_image), Player(Player2_image)     # Creation of both players
current_player = random.randint(1,2)    # Selection of first player (random)
if current_player==1:
    current_player = Player1
else:
    current_player = Player2
# current_player = Player2


# =================
# === FUNCTIONS ===
# =================

def close_game():
    pygame.display.quit()
    sys.exit()

def click_letter(m_x, m_y):             # Function to check if a click hits the circle of a letter. Returns clicked letter or None
    global letter2coord
    for letter in letter2coord.keys():
        center_letter = (letter2coord[letter][0] + radius_letter , letter2coord[letter][1] + radius_letter)
        sqx = (m_x - center_letter[0])**2
        sqy = (m_y - center_letter[1])**2

        if math.sqrt(sqx+sqy) < radius_letter:
            return letter

def draw_all(end_f):        # Function to draw everything on the screen
    global current_player, time_left, winner    # Bring these variables inside the function (they are needed)
    
    screen.blit(current_player.fondo, (0,0))            # Draw background

    screen.blit(current_player.image, (500, 175))       # Draw center image of the current player

    if button_state == 0:       # Draw button depending on its state
        screen.blit(current_player.unpressed_button, (pasapalabra_x, pasapalabra_y))
    else:
        screen.blit(current_player.pressed_button, (pasapalabra_x, pasapalabra_y))
        
    screen.blit(pasapalabra_text, (pasapalabra_x+48, pasapalabra_y+55))         # Draw PASAPALABRA

    if time_left>5:     # Change color of time rectangle if time is below 5
        screen.blit(current_player.rectangle, (score_rectangle_x, score_rectangle_y))
    else:
        screen.blit(red_rectangle, (score_rectangle_x, score_rectangle_y))

    time_left_text = time_font_75.render(str(time_left), False, white)
    screen.blit(time_left_text, (score_rectangle_x+80, score_rectangle_y+170))  # Draw time left

    screen.blit(current_player.rosco, (rosco_x, rosco_y))                       # Draw rosco

    # Here we check the dictionary of the current player to see which letters are either green or red so that they are drawn on top of the rosco
    for letter in current_player.letters2state.keys():      
        if current_player.letters2state[letter]  ==1:
            screen.blit(verde_letter2image["verde_{}".format(letter)], letter2coord[letter]) 
        elif current_player.letters2state[letter]==2:
            screen.blit(rojo_letter2image["rojo_{}".format(letter)], letter2coord[letter])

    pygame.display.flip()       # Make everything drawn appear on the screen



# ============
# === MAIN ===
# ============
while not game_end:     # While the game hasn't ended...
    clock.tick(CT)      # Speed of the game
    
    mouse_x, mouse_y = pygame.mouse.get_pos()   # Coordinates of the cursor
    time_left= max_time - time_spent


    if not pausa:       
        if not music:       # If game is not paused, music plays
            music = True
            pygame.mixer.music.play(loops=-1)
        if time_left == 0:  # If time has ended, activate pause
            pausa = True
            wrong_sfx.play()    # Play "wrong" sound effect
            pygame.mixer.music.stop()
        time_spent = (pygame.time.get_ticks()-start_ticks)//1000    # Computes time spent, which is the difference of current ticks and start ticks (divided by 1000 to obtain seconds, since ticks are miliseconds)

    Player1.is_Any0 = True   # True: there are letters in blue| False: there are no letters in blue (all either green or red)
    Player2.is_Any0 = True   # True: there are letters in blue| False: there are no letters in blue (all either green or red)

    for event in pygame.event.get():    # Check possible actions/events (mouse clicks, key presses, etc)
        if event.type==pygame.QUIT:     # Close game (press "X" on the window)
            close_game()
        if event.type == pygame.MOUSEBUTTONDOWN:    # Checks clisk of the mouse
            possible_letter = click_letter(mouse_x, mouse_y)    # Checks if the click is on a letter
            if possible_letter != None:     # Is the click WAS on a letter
                Player1.is_Any0 = False
                Player2.is_Any0 = False

                if event.button == 1:       # Turn green - Left click
                    current_player.letters2state[possible_letter] = 1
                    time_spent = 0
                    correct_sfx.play()
                elif event.button == 3:     # Turn red - Right click
                    current_player.letters2state[possible_letter] = 2
                    pausa = True
                    pygame.mixer.music.stop()
                    music = False
                    wrong_sfx.play()

                elif event.button == 2:     # Turn blue - Middle click
                    current_player.letters2state[possible_letter] = 0
                
                for letter in abecedario:   # Check if there are still letters without changes (blue letters, state = 0)
                    if Player1.letters2state[letter]==0:
                        Player1.is_Any0 = True
                    if Player2.letters2state[letter]==0:
                        Player2.is_Any0 = True
                
            else:
                if time_left != 0:      # If there's still time left, game is not paused
                    pausa = False
                else:                   # When a pause happens, reset parameters
                    start_ticks = pygame.time.get_ticks()
                    time_spent = 0
                    pausa = True
            if time_spent == 0:
                start_ticks = pygame.time.get_ticks()

            # If the click hits the PASAPALABRA button, change the button state to 1
            if pasapalabra_x < mouse_x < pasapalabra_x+pasapalabra_width and pasapalabra_y < mouse_y < pasapalabra_y+pasapalabra_height:
                button_state = 1
        elif event.type == pygame.MOUSEBUTTONUP:    # When you raise your finger from the mouse after a click
            button_state = 0    # Return button state to 0 (unclicked)

            # If pressing PASAPALABRA button:
            if pasapalabra_x < mouse_x < pasapalabra_x+pasapalabra_width and pasapalabra_y < mouse_y < pasapalabra_y+pasapalabra_height:
                # Change player
                if current_player == Player1:
                    if not Player2.end:
                        current_player = Player2
                        pausa = True
                        pygame.mixer.music.stop()
                        music = False

                else:
                    if not Player1.end:
                        current_player = Player1
                        pausa = True
                        pygame.mixer.music.stop()
                        music = False
                
                start_ticks = pygame.time.get_ticks()
                time_spent = 0
    # If a player has completed all their letters, the current player will always be the other player
    if Player1.end:
        current_player=Player2
    if Player2.end:
        current_player=Player1
    
    # END GAME
    if Player1.end and Player2.end:     # If both players have ended...
        game_end = True
        Player1_fallos, Player2_fallos = 0, 0
        for letter in abecedario:       # Count mistakes (red letters -> state = 2)
            if Player1.letters2state[letter]==2:
                Player1_fallos+=1
            if Player2.letters2state[letter]==2:
                Player2_fallos+=1
        # The winner will be the one with less mistakes (if it is the same, winner will remain being None)
        if Player1_fallos<Player2_fallos:
            winner = Player1
        elif Player1_fallos>Player2_fallos:
            winner = Player2
    
    draw_all(game_end)      # "Draw everything" funciton

    # If there are no blues left, that player has ended
    if not Player1.is_Any0:
        Player1.end=True
    if not Player2.is_Any0:
        Player2.end=True

# FINAL SCREEN
while True:
    screen.blit(current_player.fondo, (0,0))    # Draw background
    if winner is not None:      # There is winner
        screen.blit(winner.image, (500, 200))
        screen.blit(congratulations, (screen_width//4, 10))
    else:                       # There is no winner (tie)
        screen.blit(Player2.image, (screen_width*0.05, 200))
        screen.blit(Player1.image, (screen_width*0.70, 200))
        
        screen.blit(empate_text, (screen_width*0.4-40, screen_height*0.5-15))
    pygame.display.flip()

    for event in pygame.event.get():    # Close the game if the "X" is pressed
        if event.type==pygame.QUIT:
            close_game()