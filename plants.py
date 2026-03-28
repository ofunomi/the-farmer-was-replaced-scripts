# ======================================
# Plants Module
# Helper functions for crop planting
# Author: OFUNOMI
# ======================================

import location

plants = {
	'Grass': Entities.Grass,
	'Bush': Entities.Bush,
	'Carrot': Entities.Carrot,
	'Sunflower': Entities.Sunflower,
	'Pumpkin': Entities.Pumpkin,
	'Tree': Entities.Tree
}
need_to_till = ['Carrot', 'Pumpkin', 'Sunflower']


# Function: for_each_cell(start, end, action)
# Use: for_each_cell(start=(0,0), end=(4,4), action=some_function)
# Description: action must be a function with x and y parameters
#
# What it does:
# - moves through each cell in the specified zone
# - runs the selected action on each cell

def for_each_cell(start, end, action):
	for x in range(start[0], end[0] + 1):
		for y in range(start[1], end[1] + 1):
			location.move_to(x, y)
			action(x, y)


# Function: measure_zone(start, end)
# Use: measure_zone(start=(0,0), end=(4,4))
# Description: collects measure() values from the specified zone
#
# What it does:
# - visits each cell in the specified zone
# - stores the measure value and its coordinates

def measure_zone(start, end):
	values = []

	def collect_measurement(x, y):
		values.append([measure(), (x, y)])

	for_each_cell(start, end, collect_measurement)
	return values


# Function: try_harvest()
# Use: try_harvest()
# Description: harvests the current cell if it is ready
#
# What it does:
# - checks whether the current cell can be harvested
# - harvests it if possible

def try_harvest(x=None, y=None):
	if can_harvest():
		harvest()


# Function: harvest_zone(start, end)
# Use: harvest_zone(start=(0,0), end=(4,4))
# Description: harvests all ready plants in the specified zone
#
# What it does:
# - visits each cell in the specified zone
# - harvests every ready plant

def harvest_zone(start, end):
	for_each_cell(start, end, try_harvest)


# Function: harvest_sunflower(start, end)
# Use: harvest_sunflower(start=(0,0), end=(4,4))
# Description: harvests sunflowers in order of highest measure()
#
# What it does:
# - gets all measure values in the specified zone
# - harvests the best sunflower first

def harvest_sunflower(start, end):
	values = measure_zone(start, end)
	for i in range(len(values)):
		best = max(values)
		x, y = best[1]
		values.remove(best)
		location.move_to(x, y)
		try_harvest()


# Function: harvest_plants(plan)
# Use: harvest_plants(plan)
#
# Description:
# - plan must be a dictionary
# - each key must be a plant name
# - each value must be ((start_x, start_y), (end_x, end_y))
#
# Example:
# plan = {
#     'Carrot': ((0, 0), (2, 15)),
#     'Sunflower': ((3, 0), (5, 15))
# }
#
# What it does:
# - checks each zone from the plan
# - uses special harvest logic for Sunflower


def harvest_plants(plan):
	for name in plan:
		start, end = plan[name]
		if name == 'Sunflower':
			harvest_sunflower(start, end)
		else:
			harvest_zone(start, end)

# Function: planting(name)
# Use: planting('Carrot')
# Description: name must be a key from the plants dictionary
#
# What it does:
# - tills the ground if needed
# - plants the selected crop

def planting(name):
	if name in need_to_till and get_ground_type() != Grounds.Soil:
		till()
	if get_water() < 0.5:
		use_item(Items.Water)
	plant(plants[name])

# Function: plant_in_zone(start, end, name)
# Use: plant_in_zone(start=(0,0), end=(4,4), name='Grass')
# Description: name must be a key from the plants dictionary
#
# What it does:
# - plants the selected crop in the specified zone

def plant_in_zone(start, end, name):
	if name == 'Grass':
		return
	
	def plant_in_cell(x, y):
		if name == 'Tree' and (x + y) % 2 == 0:
			planting('Grass')
		else:
			planting(name)

	for_each_cell(start, end, plant_in_cell)
