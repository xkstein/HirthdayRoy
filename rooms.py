class Room():
    def __init__(self, x, y, items):
        self.x = x
        self.y = y
        self.items = items{}
    def intro(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplemented()

class StartingRoom(Room):
    items = {knife}
    def intro(self):
        return """
        You find yourself in a small grey appartment room.
        There's a locked window with the shutters drawn,
        and a simple door in front of you. There's a knife on the floor.
        """
    def modify_player(self, player)
        pass
    
    
