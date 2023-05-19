import numpy
import random
from room import Room
from field import Field

field_size = 9
base_field = Field(field_size)

def generation(count=10, size=field_size, return_html_field=False):
    tmp_field = Field(size)
    tmp_field.place_room(int(size/2),int(size/2))
    for i in range(count):
        whitelist = []
        for x in range(len(tmp_field)):
            for y in range(len(tmp_field[x])):
                if  tmp_field[x][y].is_free: whitelist.append([x,y])
        random_cell = random.choice(whitelist)
        tmp_field.place_room(random_cell[0], random_cell[1])
        print(f"placed on ({random_cell[0]},{random_cell[1]})")
    print(tmp_field)
    if return_html_field: return create_html_field(tmp_field, size)
    return tmp_field


def create_html(field=base_field, size=field_size):
    html = "<table>"
    for y in range(len(field)):
        html += "<tr>"
        for x in range(len(field[y])):
            html += f"<td onclick=send({y},{x}) class="
            
            if field[x][y].is_empty: 
                if [x, y] in field.white_list: html += "free"
                else: html += "empty"
            elif field[x][y].is_locked: html += "lock"
            else: html += "used"
            
            html += f">{field[x][y].place_id if field[x][y].place_id != None else ''}</td>"

        html += "</tr>"
    html += "</table>"
    return html

def create_html_field(field=base_field, size=field_size):
    tmp_field = []
    
    for x in range(size):
        tmp_field.append([])
        for y in range(size):
            if field[x][y].is_empty: tmp_field[x].append(["empty", field[x][y].place_id])
            elif field[x][y].is_free: tmp_field[x].append(["free", field[x][y].place_id])
            elif field[x][y].is_locked: tmp_field[x].append(["lock", field[x][y].place_id])
            else: tmp_field[x].append(["used", field[x][y].place_id])
                
    return tmp_field