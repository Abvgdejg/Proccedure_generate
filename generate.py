import numpy
import random
from room import Room
from field import Field

# field_size = 9
# center_int = int(field_size / 2)
# center_coord = (center_int, center_int)
# free_coords = []
# busy_coords = []
# blacklist = []
# # cootds_list = [(x,y) for x in range(field_size) for y in range(field_size)]
# field = numpy.zeros((field_size,field_size))

# def check_blacklist(last_coord):
#     x = last_coord[1]
#     y = last_coord[0]
#     check_list = [(y, x+1),(y, x-1), (y+1, x), (y-1, x)]
#     for coord in check_list:
#         t_x = coord[1]
#         t_y = coord[0]
#         tmp_check_list = [(t_y, t_x+1),(t_y, t_x-1), (t_y+1, t_x), (t_y-1, t_x)]
#         for s_coord in tmp_check_list:
#             if s_coord in busy_coords and \
#                s_coord != last_coord and \
#                s_coord not in blacklist: 
#                 blacklist.append(coord)
#                 break
        
#     print(f'blist: {blacklist}')
            

# def check_free(last_coord):
#     x = last_coord[1]
#     y = last_coord[0]
#     check_list = [(y, x+1),(y, x-1), (y+1, x), (y-1, x)]
#     for coord in check_list:
#         if field[coord] == 0 and coord not in blacklist: free_coords.append(coord)
        
#     print(f'wlist: {free_coords}')

# def start_generate(count = 10):
#     for i in range(count):
#         random_coord = random.choice(free_coords)
#         place_room(random_coord)

# def place_room(coord):
#     field[coord] = 1
#     busy_coords.append(coord)
    
#     check_blacklist(coord)
#     check_free(coord)
#     # try:
#     #     free_coords.remove(coord)
#     # except: print("Hasn't in wlist")

#     print(f'placed: {coord}')



# place_room(center_coord)

# start_generate()

field = Field(9)
field.check_free_rooms(Room(4,4))
print(field.white_list)
print(field)