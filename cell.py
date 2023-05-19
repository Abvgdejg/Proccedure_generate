class Status():

        empty = "empty"
        locked = "locked"
        used = "used"
        free = "free"

class Cell():

    status = None
    contains = None

    connections = 0

    place_id = None
    x = 0
    y = 0

    def __init__(self, x=0, y=0, place_id=None, contains=None, status:Status = Status.empty):
        self.status = status
        self.contains = contains

        self.place_id = place_id

        self.x = x
        self.y = y

    def set(self, contains):
        self.contains = contains
        self.status = Status.used

    def change_state(self, status: Status):
        self.status = status


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
    def is_free(self):
        return self.status == Status.free
        

    @property
    def max_connected(self):
        return self.connections >= 2

    @property
    def state(self):
        return self.status