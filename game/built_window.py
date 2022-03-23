"""
raylib [core] example - Basic window

"""
from raylib.colors import (RAYWHITE,LIGHTGRAY,RED,DARKGRAY)
import pyray

from game.mouse import Mouse

# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
class BuiltWindow:
    def __init__(self):
        pass
    pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,'TEAM - CSE210-01')
    pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second


    # Main game loop
    while not pyray.window_should_close():  # Detect window close button or ESC key
        # Update
        # TODO: Update  variables FOR THE GAME here!
        Mouse()#empezar a detectar lo que hace el mouse

        # Draw
        pyray.begin_drawing()

        pyray.clear_background(RED)
        pyray.draw_text(
            'This is our window !', 190, 200, 26, LIGHTGRAY)

        pyray.end_drawing()


    # De-Initialization
    pyray.close_window()  # Close window and OpenGL context,
                          #Check if KEY_ESCAPE pressed or Close icon pressed
