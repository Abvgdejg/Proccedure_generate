from cell import Status, Cell
import random

class Field():

    def __init__(self, size = 9, gen_count = 10, whitelist = []):
        self.size = size
        self.gen_count = gen_count
        self.field = self.create_field()
        self.whitelist = whitelist

    def create_field(self):
        grid_cells = []
        for x in range(self.size):
            grid_cells.append([])
            for y in range(self.size):
                grid_cells[x].append(Cell(x, y))
        
        return grid_cells

    def place_room(self, x,y, id):
        self.field[x][y].status = "used"
        self.field[x][y].id = id

        neighbors = [[x, y - 1], [x + 1, y],
                    [x, y + 1], [x - 1, y]]
        for neighbor in neighbors:
            x, y = neighbor[0], neighbor[1]
            if x < 0 or x > self.size - 1 or y < 0 or y > self.size - 1:
                continue
            
            cell = self.field[x][y]
            cell.connections += 1
            if  cell.connections >= 2 and cell.status != "used": 
                if [x,y] in self.whitelist: self.whitelist.remove([x,y])
                cell.status = "banned" 



    def update_whitelist(self, x,y):
        neighbors = [[x, y - 1], [x + 1, y],
                    [x, y + 1], [x - 1, y]]
        for neighbor in neighbors:
            x, y = neighbor[0], neighbor[1]
            if x < 0 or x > self.size - 1 or y < 0 or y > self.size - 1:
                continue

            if  self.field[x][y].status != "banned" \
                and self.field[x][y].status != "used" \
                and ([x,y] not in self.whitelist):
                    self.whitelist.append([x,y])
                    self.field[x][y].status = "free"
        

    def reqursive_gen(self, iteration_count = "auto"):
        if iteration_count == "auto": iteration_count = self.gen_count
        if iteration_count <= 0: return self.field
        else: iteration_count -= 1

        next_cell = random.choice(self.whitelist)
        x, y = next_cell[0], next_cell[1]

        self.whitelist.remove(next_cell)
        self.place_room(x,y, iteration_count)

        self.update_whitelist(x,y) 

        return self.reqursive_gen(iteration_count)

    def show_field(self) -> str:
            res = ""
            for x in range(len(self.field)):
                for y in range(len(self.field[x])):
                    if self.field[x][y].status == None: res += "0"
                    elif self.field[x][y].status == "free": res += "f"
                    elif self.field[x][y].status == "banned": res += "b"
                    else: res += "1"
                    res += " | "
                res += "\n"   
            
            return res

    def mono_gen(self):
        self.reqursive_gen(1)
        return self.field
