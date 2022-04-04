from constants import *
from game.scripting.action import Action


class ControlBoyAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        boy = cast.get_first_actor(BOY_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            boy.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            boy.swing_right()  
        else: 
            boy.stop_moving()