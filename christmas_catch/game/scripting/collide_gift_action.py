from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideGiftAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        #santa = cast.get_first_actor(SANTA_GROUP)
        boy = cast.get_first_actor(BOY_GROUP)
        gifts = cast.get_actors(GIFT_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        gift = cast.get_first_actor(GIFT_GROUP)
        body = gift.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()       
        over_sound = Sound(OVER_SOUND)
        red_gift = GIFT_IMAGES['p'] 
        
        for gift in gifts:
            boy_body = boy.get_body()
            gift_body = gift.get_body()

            if self._physics_service.has_collided(boy_body, gift_body):
                #santa.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = gift.get_points()
                stats.add_points(points)
                cast.remove_actor(GIFT_GROUP, gift)
            
            # elif self._physics_service.has_collided(racket_body, red_gift):
            #     points = gift.get_points()
            #     stats.rest_point(points)
            #     cast.remove_actor(GIFT_GROUP, gift)

            elif y >= (SCREEN_HEIGHT):
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
            
                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN) 
                else:
                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(over_sound)
            
            