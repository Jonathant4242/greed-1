#new code
#from shared.point import Point
#from point import Point
from game.shared.point import Point
#end new 

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)    

        #new code
        objects = cast.get_actors('objects')
        for object in objects:
            velocity = self._keyboard_service.move_down()
            object.set_velocity(velocity)
        # end new code    

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with objects.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        objects = cast.get_actors("objects")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        #new code
        objects = cast.get_actors('objects')
        for object in objects:
            object.move_next(max_x, max_y)
        #end new code
        
    #     #new code here, need to get each object, loop through, adding to its y coordiante each time. This should make it move down.    
    # #for i in cast.get_actors("objects"):
    # #    pass    
    #     #objects = cast.get_actors("objects")
        
    #     for object in objects:
    #         #position = object.get_position()
    #         #movement = Point(0, 1)
    #         object.move_next(900, 600)
    #         #object.move_next(0, 1)

    #         #end of new code


        for object in objects:
            if robot.get_position().equals(object.get_position()):
                message = object.get_message()
                banner.set_text(message)    
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()