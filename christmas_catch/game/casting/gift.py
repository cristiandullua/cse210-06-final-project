from constants import *
from game.casting.image import Image
from game.casting.actor import Actor
from game.casting.point import Point


class Gift(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, type_of_gift = 0, debug = False):
        """Constructs a new Gift.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = 0
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

        self._type_of_gift = type_of_gift
        #GREEN GIFT
        if type_of_gift == 0:
            self._image = Image(GIFT_GREEN_IMAGES)
            self.set_points(GIFT_GREEN_POINTS) 
        #RED GIFT
        elif type_of_gift == 1:
            self._image = Image(GIFT_RED_IMAGES)
            self.set_points(GIFT_RED_POINTS)
        #COAL
        elif type_of_gift == 2:
            self._image = Image(COAL_IMAGE)
            self.set_points(COAL_POINTS) 

    def get_type(self):
        return self._type_of_gift

    def get_body(self):
        """Gets the gift's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the gift's points.
        
        Returns:
            A number representing the gift's points.
        """
        return self._points

    def get_image(self):
        """Gets the santa's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def bounce_x(self):
        """Bounces the santa in the x direction."""
        velocity = self._body.get_velocity()
        vx = velocity.get_x() * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)
