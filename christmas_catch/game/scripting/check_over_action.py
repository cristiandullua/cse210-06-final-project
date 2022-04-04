from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        gifts = cast.get_actors(GIFT_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        if len(gifts) == 0 or stats.get_lives() == 0:
            callback.on_next(GAME_OVER)