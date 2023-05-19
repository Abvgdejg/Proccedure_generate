from room import Room
from cell import Status, Cell

class Field():


    def __init__(self, size = 5):
        self.field = []

        self.rooms_list = []

        self.black_list = []
        self.white_list = []

        self.place_counter = 0

        for x in range(size):
            self.field.append([])
            for y in range(size):
                self.field[x].append(Cell(x=x, y=y))

        print(len(self.field), self.rooms_list, self.black_list, self.white_list)

    def place_room(self, y, x):
        
        self.field[x][y].set(Room())
        self.field[x][y].place_id = self.place_counter
        self.field[x][y].change_state(Status.used)
        self.place_counter += 1

        self.place_handler(x,y)


    def place_handler(self, x,y):
        
        check_list = [[x+1, y],[x-1, y], [x, y+1], [x, y-1]]
        for x, y in check_list:
            self.check_for_blacklist(x,y)
            self.check_for_whitelist(x,y)
            

    def check_for_whitelist(self, x,y):
        cell = self.field[x][y]
        if cell.is_free: return
        if cell.is_empty: cell.change_state(Status.free)

    def check_for_blacklist(self, x,y):
        cell = self.field[x][y]
        if cell.is_locked: return
        if cell.is_free: cell.connect()
        if cell.max_connected: cell.change_state(Status.locked)

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
