from room import Room
from cell import Status, Cell

class Field():

    field = []

    rooms_list = []

    black_list = []
    white_list = []

    def __init__(self, size = 5):
        
        for x in range(size):
            self.field.append([])
            for y in range(size):
                self.field[x].append(Cell(x=x, y=y))

        print(len(self.field))




    def place_room(self, y, x):
        
        self.rooms_list.append([x,y])
        self.field[x][y].set(Room())
        try:
            self.white_list.remove([x,y])
        except:pass

        self.place_handler(x,y)


    def place_handler(self, x,y):
        
        check_list = [[x+1, y],[x-1, y], [x, y+1], [x, y-1]]
        for x, y in check_list:
            self.check_for_blacklist(x,y)
            self.check_for_whitelist(x,y)
            

    def check_for_whitelist(self, x,y):
        if self.field[x][y].is_empty and \
            [x, y] not in self.white_list and \
            not self.field[x][y].is_locked:
                self.white_list.append([x, y])

    def check_for_blacklist(self, x,y):
        self.field[x][y].connect()
        if self.field[x][y].max_connected and \
           not self.field[x][y].is_used: 
                self.add_to_blacklist(x,y)

    def add_to_blacklist(self, x,y):
        self.black_list.append([x, y])
        try:
            self.white_list.remove([x, y])
        except:pass
        self.field[x][y].status = Status.locked
    
    def __repr__(self) -> str:
        res = ""
        for x in range(len(self.field)):
            for y in range(len(self.field[x])):
                if self.field[x][y].is_empty: 
                    if [x, y] in self.white_list: res += "f"
                    else: res += "0"
                elif self.field[x][y].is_locked: res += "b"
                else: res += "1"
                res += " | "
            res += "\n"   
        
        return res

    def __getitem__(self, key):
        return self.field[key]

    def __len__(self):
        return len(self.field)   
