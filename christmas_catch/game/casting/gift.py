import random
from game.casting.actor import Actor
from game.casting.point import Point


class Gift(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, animation, points, cols = 60, rows = 40, cell_size = 15, debug = False):
        """Constructs a new Gift.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points
        x = random.randint(1, cols - 1)
        y = random.randint(1, rows - 1)
        position = Point(x, y)
        position = position.scale(cell_size)

        
        
    def get_animation(self):
        """Gets the gift's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

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