from game.casting.point import Point


class Actor:
    """A thing that participates in the game."""
    
    def __init__(self, debug = False):
        """Constructs a new Actor using the given group and id.
        
        Args:
            group: A string containing the actor's group name.
            id: A number that uniquely identifies the actor within the group.
        """
        self._debug = debug
        self._points = 0        
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        
    def is_debug(self):
        """Whether or not the actor is being debugged.
        
        Returns:
            True if the actor is being debugged; False if otherwise.
        """
        return self._debug

    def get_points(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The actor's text color.
        """
        return self._points

    def set_points(self, points):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._points = points
    ###

     
    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    ### Position bottom
    def get_position_bottom(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        x = self._position._x
        y = self._position._y 
        return Point(x, y)
    ###    
    
    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def move_next(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    
    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
        
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
