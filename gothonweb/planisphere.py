# A game to be tested. 
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

room = Room('Ulf', 'pappa')
#room.go = 'east'
print(room.name)
print(type(room.paths))
print(room.go)
