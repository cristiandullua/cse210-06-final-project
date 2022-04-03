from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBoyAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        santa = cast.get_first_actor(SANTA_GROUP)
        boy = cast.get_first_actor(BOY_GROUP)
        
        santa_body = santa.get_body()
        boy_body = boy.get_body()

        if self._physics_service.has_collided(santa_body, boy_body):
            #santa.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)    