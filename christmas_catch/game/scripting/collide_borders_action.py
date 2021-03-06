from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.image import Image
from game.casting.santa import Santa


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
            cast.clear_actors (SANTA_GROUP)            
            image = Image(SANTA_IMAGE)
            santa = Santa(body, image, True)
            cast.add_actor(SANTA_GROUP, santa)
            
        elif x >= (FIELD_RIGHT - SANTA_WIDTH):
            santa.bounce_x() 
            self._audio_service.play_sound(bounce_sound)
            cast.clear_actors(SANTA_GROUP)            
            image = Image(SANTA_COMEBACK)
            santa = Santa(body, image, True)
            cast.add_actor(SANTA_GROUP, santa)

        gifts = cast.get_actors(GIFT_GROUP)
        for gift in gifts:
            body_g = gift.get_body()
            position_g = body_g.get_position()
            x_g = position_g.get_x()
            y_g = position_g.get_y()
                    
            if x_g < FIELD_LEFT:
                gift.bounce_x()
            elif x_g >= (FIELD_RIGHT - GIFT_WIDTH):
                gift.bounce_x() 

            if y_g > FIELD_BOTTOM:
                cast.remove_actor(GIFT_GROUP, gift)