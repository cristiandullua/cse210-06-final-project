from constants import *
from game.scripting.action import Action


class MoveSantaAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        santa = cast.get_first_actor(SANTA_GROUP)
        body = santa.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
