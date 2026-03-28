# Function: move_to_x(x)
# Use: move_to_x(x=0)
# Description: moves to the selected x coordinate
#
# What it does:
# - checks the current x position
# - moves using the shorter wrapped path

def move_to_x(x=0):
	del_x = get_pos_x() - x
	if get_world_size() - abs(del_x) < abs(del_x):
		del_x = -1 * del_x
	while get_pos_x() != x:
		if del_x > 0:
			move(West)
		else: 
			move(East)
			

# Function: move_to_y(y)
# Use: move_to_y(y=0)
# Description: moves to the selected y coordinate
#
# What it does:
# - checks the current y position
# - moves using the shorter wrapped path

def move_to_y(y=0):
	del_y = get_pos_y() - y
	if get_world_size() - abs(del_y) < abs(del_y):
		del_y = -1 * del_y
	while get_pos_y() != y:
		if del_y > 0:
			move(South)
		else: 
			move(North)			

			
# Function: move_to(x, y)
# Use: move_to(x=0, y=0)
# Description: moves to the selected cell
#
# What it does:
# - moves to the selected x coordinate
# - moves to the selected y coordinate

def move_to(x=0, y=0):
	move_to_x(x)
	move_to_y(y)
