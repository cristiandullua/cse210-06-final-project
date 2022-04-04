from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        santa = cast.get_first_actor(SANTA_GROUP)
        body = santa.get_body()
        position = body.get_position()
        x = position.get_x()
        bounce_sound = Sound(BOUNCE_SOUND)
                
        if x < FIELD_LEFT:
            santa.bounce_x()
            self._audio_service.play_sound(bounce_sound)
        elif x >= (FIELD_RIGHT - SANTA_WIDTH):
            santa.bounce_x() 
            self._audio_service.play_sound(bounce_sound)

        gifts = cast.get_actors(GIFT_GROUP)
        for gift in gifts:
            body_g = gift.get_body()
            position_g = body_g.get_position()
            x_g = position_g.get_x()
                    
            if x_g < FIELD_LEFT:
                gift.bounce_x()
                self._audio_service.play_sound(bounce_sound)
            elif x_g >= (FIELD_RIGHT - GIFT_WIDTH):
                gift.bounce_x() 
                self._audio_service.play_sound(bounce_sound)