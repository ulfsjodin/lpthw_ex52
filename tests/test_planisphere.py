#Pytest will be my choice for this exercise.

import pytest
from ex47 import game

def test_Room():
    room = game.Room('GoldRoom', 
    """This room has gold in it you can grab. There is a door to the north.""")
    assert room.name == 'GoldRoom'
    assert room.paths == {} 

def test_room_paths():
    center = game.Room('Center','Test room in the center')
    north = game.Room('North','Test room in the north')
    south = game.Room('South','Test room in the south')
    center.add_paths({'north': north, 'south': south})

    assert center.go('south') == south
    assert center.go('north') == north

def test_map():
    start = game.Room("Start", "You can go west and fall down in a cave")
    west = game.Room("Trees", "There are only trees here, you can go east.")
    down = game.Room("Dungeon", "how did you get here? Get back to the game!")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start
