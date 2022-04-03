from constants import *
from game.scripting.action import Action


class MoveGiftsAction(Action):
 

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        gift = cast.get_first_actor(GIFT_GROUP)
        body = gift.get_body()
        position = body.get_position()
        velocity = body.get_velocity()        
        position = position.add(velocity)
        body.set_position(position)
