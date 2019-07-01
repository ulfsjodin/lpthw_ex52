# Pytest will be my choice for this exercise.
import gothonweb
from gothonweb import planisphere
from gothonweb.planisphere import START, load_room, generic_death, laser_weapon_armory, central_corridor


def test_Room():
    room = planisphere.Room('GoldRoom',
    """This room has gold in it you can grab. There is a door to the north.""")
    assert room.name == 'GoldRoom'
    assert 'This room has gold' in room.description
    assert room.paths == {} 

def test_room_paths():
    center = planisphere.Room('Center','Test room in the center')
    north = planisphere.Room('North','Test room in the north')
    south = planisphere.Room('South','Test room in the south')
    center.add_paths({'north': north, 'south': south})

    assert center.go('south') == south
    assert center.go('north') == north

def test_map():
    start = planisphere.Room("Start", "You can go west and fall down in a cave")
    west = planisphere.Room("Trees", "There are only trees here, you can go east.")
    down = planisphere.Room("Dungeon", "how did you get here? Get back to the planisphere!")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start

def test_gothon_game_map():
    start_room = planisphere.load_room(START)
    assert start_room.go('dodge') == generic_death

    room = start_room.go('tell a joke')
    assert  room == laser_weapon_armory

def test_load_room():
    assert globals().get(central_corridor) == None
