from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        #ball = cast.get_first_actor(BALL_GROUP)
        racket = cast.get_first_actor(RACKET_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        brick = cast.get_first_actor(BRICK_GROUP)
        body = brick.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()       
        over_sound = Sound(OVER_SOUND)
        
        for brick in bricks:
            racket_body = racket.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(racket_body, brick_body):
                #ball.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)
                
            elif y >= (SCREEN_HEIGHT):
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
            
                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN) 
                else:
                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(over_sound)
            
            