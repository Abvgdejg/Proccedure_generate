from room import Room

class Field():

    field = []

    rooms_list = []

    black_list = []
    white_list = []

    def __init__(self, size = 5):
        for x in range(size):
            self.field.append([])
            for y in range(size):
                self.field[x].append(None)

        self.place_room(Room(int(size/2),int(size/2)))


    def place_room(self, room):
        x = room.x
        y = room.y

        self.rooms_list.append(room)
        self.field[x][y] = Room(x, y)


    def check_free_rooms(self, last_room):
        x = last_room.x
        y = last_room.y
        check_list = [[y, x+1],(y, x-1), (y+1, x), (y-1, x)]
        for x, y in check_list:
            if self.field[x][y] == None and \
               [x, y] not in self.white_list:
                self.white_list.append([x, y])

    
    def __repr__(self) -> str:
        res = ""
        for x in range(len(self.field)):
            for y in range(len(self.field[x])):
                res += ("1" if self.field[x][y] != None else "f" if [x, y] in self.white_list else "0") + " | "
            res += "\n"   
        
        return res

    def __len__(self):
        return len(self.field)   
