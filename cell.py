class Status():

        empty = "empty"
        locked = "locked"
        used = "used"

class Cell():

    status = None
    contains = None

    connections = 0

    x = 0
    y = 0

    def __init__(self, x=0, y=0, contains=None, status:Status = Status.empty):
        self.status = status
        self.contains = contains

        self.x = x
        self.y = y

    def set(self, contains):
        self.contains = contains
        self.status = Status.used

    def connect(self):
        self.connections += 1

    @property
    def is_empty(self):
        return self.status == Status.empty

    @property
    def is_locked(self):
        return self.status == Status.locked

    @property
    def is_used(self):
        return self.status == Status.used
        
    
    @property
    def max_connected(self):
        return self.connections >= 2

    
