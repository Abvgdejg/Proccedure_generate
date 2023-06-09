import random
from field import Field

r = random.Random()

saved_field = None

def generation(gen_count, size, return_html_field=False):
    global saved_field
    saved_field = Field(size, gen_count, [[int(size/2),int(size/2)]])
    tmp_field = saved_field.reqursive_gen()
    if return_html_field: return create_html_field(tmp_field, size)
    return tmp_field

def add_gen():

    tmp_field = saved_field.mono_gen()

    return create_html_field(tmp_field, saved_field.size)
    return tmp_field

def create_html_field(field, size):
    tmp_field = []

    for x in range(size):
        tmp_field.append([])
        for y in range(size):
            if field[x][y].status == None: tmp_field[x].append(["empty", field[x][y].id])
            elif field[x][y].status == "free": tmp_field[x].append(["free", field[x][y].id])
            elif field[x][y].status == "banned": tmp_field[x].append(["lock", field[x][y].id])
            else: tmp_field[x].append(["used", field[x][y].id])
    
    return tmp_field