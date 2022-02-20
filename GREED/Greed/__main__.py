import os
import random

from game.casting.actor import Actor
from game.casting.object import Object
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point



FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Robot Finds Kitten"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_OBJECTS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(575)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the objects

    #this is getting the data file of random messages, reading it line by line, spliting it up, and returing each line as the message that's displayed when the robot hits the object.

    #This can be deleted because the new game won't have messages displayed. instead it needs to have points added or subtracted when o/x are hit.
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    #this is looping through 40 times (number of default_artifacts)
    for n in range(DEFAULT_OBJECTS):
        #this picks a random number, and gets the symbol associated with that number in unicode alphabet thingy. This is whats generating the random symbols for the objects.
        #this needs to be changed to just give x and o objects. 
        text = chr(random.choice([42, 79]))
        #this is assigning a message to each of the n objects
        message = messages[n]

        #this is generating a random x/y position that will be used to put the objects in random places on the screen
        #maybe add some kind of loop to add to the y position to make them move down the screen.
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)   
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        object = Object()
        object.set_text(text)
        object.set_font_size(FONT_SIZE)
        object.set_color(color)
        object.set_position(position)
        object.set_message(message)
        cast.add_actor("objects", object)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()