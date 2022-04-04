from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideGiftAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        boy = cast.get_first_actor(BOY_GROUP)
        gifts = cast.get_actors(GIFT_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        for gift in gifts:
            boy_body = boy.get_body()
            gift_body = gift.get_body()
            
            if self._physics_service.has_collided(boy_body, gift_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = gift.get_points()
                stats.add_points(points)
                if gift.get_type() == 2: #COAL
                    stats.lose_life()
                cast.remove_actor(GIFT_GROUP, gift)