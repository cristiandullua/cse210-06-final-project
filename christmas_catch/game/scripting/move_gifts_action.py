from constants import *
from game.scripting.action import Action


class MoveGiftsAction(Action):
 

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        gifts = cast.get_actors(GIFT_GROUP)

        for gift in gifts:
            body = gift.get_body()
            position = body.get_position()
            velocity = body.get_velocity()        
            position = position.add(velocity)
            body.set_position(position)
