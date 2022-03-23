import pyray

from raylib.colors import (DARKBLUE,LIME,MAROON)

class Mouse():
    def __init__(self):
        self.ball_position = pyray.get_mouse_position()

        if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT):
            ball_color = MAROON
            print("soyyy  ",ball_color)
            print("soyyy  ",self.ball_position)
        elif pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_MIDDLE):
            ball_color = LIME
            print("soyyy  ",ball_color)
            print("soyyy  ",self.ball_position)
        elif pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_RIGHT):
            ball_color = DARKBLUE
            print("soyyy  ",ball_color)
            print("soyyy  ",self.ball_position)
