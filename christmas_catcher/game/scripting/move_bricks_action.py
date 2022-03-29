from constants import *
from game.scripting.action import Action


class MoveBricksAction(Action):
 

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        brick = cast.get_first_actor(BRICK_GROUP)
        body = brick.get_body()
        position = body.get_position()
        velocity = body.get_velocity()        
        position = position.add(velocity)
        body.set_position(position)
