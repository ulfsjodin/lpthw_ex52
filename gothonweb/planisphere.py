# Exercise 52
# A planisphere to be tested.
# In my case it will be Pytest instead of nosetest.


class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
                        """
                        The Gothons  of planet Percal #34 have indvaded your ship.....

                        """)


laser_weapon_armory = Room("Laser Weapon Armory",
                           """
                           Lucky for you they made learn Gothon insults in the academy...
                           """)


the_bridge = Room("The Bridge",
                  """
                  You point the gun at the bomb..Bridge.
                  """)

escape_pod = Room("Escape pod",
                  """
                  You point the gun at the bomb... Escape pod
                  """)


the_end_winner = Room("The End",
                      """
                      You jump into escape pod 2 and hit the eject button...
                      """)


the_end_looser = Room("The End",
                      """
                      You jump into an random escape pod and hit the eject button.... 
                      """)


escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_looser
})


generic_death = Room("death", "You died.")


the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    "*": generic_death
})

central_corridor.add_paths({
    'shoot': generic_death,
    'dodge': generic_death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'


def load_room(name):
    """
    There is a potential problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)


def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    """

    for key, value in globals().items():
        if value == room:
            return key
