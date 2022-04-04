from constants import *
from game.scripting.action import Action


class DrawBoyAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        boy = cast.get_first_actor(BOY_GROUP)
        body = boy.get_body()

        if boy.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = boy.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)