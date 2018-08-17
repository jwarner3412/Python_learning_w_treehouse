import random

#draw grid
def create_grid(size=4):
	grid=set()
	for num in range(size):
		for n in range(size):
			grid.add((num, n))
	return grid

game_grid = create_grid(5)

