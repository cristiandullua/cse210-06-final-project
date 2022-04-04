from constants import *
from game.scripting.action import Action


class DrawGiftsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        gifts = cast.get_actors(GIFT_GROUP)

        for gift in gifts:
            body = gift.get_body()

            if gift.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
            
            image = gift.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)