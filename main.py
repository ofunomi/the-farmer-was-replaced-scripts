#For 11 x 11

import plants

plan = {
    'Carrot': ((0, 0), (2, 15)),
    'Tree': ((3, 0), (5, 15)),
    'Sunflower': ((6, 0), (6, 15)),
	'Grass': ((7, 0), (10, 15)),
    'Pumpkin': ((11, 0), (15, 15)),
}

while True:
	for name in plan:
		(start, end) = plan[name]
		plants.plant_in_zone(start, end, name)
	plants.harvest_plants(plan)