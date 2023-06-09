class Status():

        empty = "empty"
        locked = "locked"
        used = "used"
        free = "free"

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.status = None
        self.connections = 0
        self.id = None
    
    def __repr__(self) -> str:
        res = f"Cell[{self.x},{self.y}]:({self.status})" 
        
        return res
    