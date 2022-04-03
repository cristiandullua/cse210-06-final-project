import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Christmas Catch"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 40
FIELD_BOTTOM = 200
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "christmas_catch/assets/fonts/zorque.otf"
FONT_FILE_LOGO = "christmas_catch/assets/fonts/font_logo.otf"
FONT_SMALL = 32
FONT_LARGE = 48
FONT_SIZE_LOGO = 60

# SOUND
BOUNCE_SOUND = "christmas_catch/assets/sounds/boing.wav"
WELCOME_SOUND = "christmas_catch/assets/sounds/christmas.mp3"
OVER_SOUND = "christmas_catch/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "christmas_catch/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# BACKGROUND
BACKGROUND_GROUP = "background"
BACKGROUND_IMAGE = "christmas_catch/assets/images/background.png"
MENU_IMAGE = "christmas_catch/assets/images/menu_background.png"

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "christmas_catch/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 3
MAX_X = 900
MAX_Y = 600

# BOY
BOY_GROUP = "boys"
BOY_IMAGES = [f"christmas_catch/assets/images/{n:03}.png" for n in range(100, 103)]
BOY_WIDTH = 120
BOY_HEIGHT = 161
BOY_RATE = 6
BOY_VELOCITY = 7

# GIFT/REGALOS
GIFT_GROUP = "gifts"
GIFT_IMAGES = {
    "b": [f"christmas_catch/assets/images/{i:03}.png" for i in range(10,11)],
    "g": [f"christmas_catch/assets/images/{i:03}.png" for i in range(104,105)],
    "p": [f"christmas_catch/assets/images/{i:03}.png" for i in range(104,105)],
    "y": [f"christmas_catch/assets/images/{i:03}.png" for i in range(104,105)]
}
GIFT_WIDTH = 50
GIFT_HEIGHT = 28
GIFT_DELAY = 0.5
GIFT_RATE = 4
GIFT_POINTS = 50

#COAL
COAL_GROUP = "coals"
COAL_IMAGE = "christmas_catch/assets/images/103.png"
COAL_WIDTH = 50
COAL_HEIGHT = 28
COAL_DELAY = 0.5
COAL_RATE = 4
COAL_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"