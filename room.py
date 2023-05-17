class Room():

    coord = None
    x = None
    y = None

    def __init__(self):
        self.coord = (0, 0)
        self.x = 0
        self.y = 0
        

    def __init__(self, x = None, y = None):
        self.x = x if x != None else 0
        self.y = y if y != None else 0
        self.coord = (x, y)
