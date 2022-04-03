import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

velocity = 6

class Santa(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Santa.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def bounce_x(self):
        """Bounces the santa in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 0)
        vx = velocity.get_x() * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the santa in the y direction"""
        velocity = self._body.get_velocity()
        #rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * -1 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_body(self):
        """Gets the santa's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the santa's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    """def release(self):
        Release the santa in a random direction.
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-SANTA_VELOCITY * rn, SANTA_VELOCITY * rn])
        vy = -SANTA_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)"""