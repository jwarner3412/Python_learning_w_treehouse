import random
import os

# Pick random location for player
# " " " " monster
# " " " " door
# Draw player on grid
# take input for movement
# move player if valid move
# check for win/loss
# clear screen and redraw grid

# Draw grid
def create_grid(size=4):
	grid=[]
	for num in range(size):
		for n in range(size):
			grid.append((num, n))
	return grid

def get_locations(grid):
	#get the players location
	return random.sample(grid, 3)

def move_player(player, move):
	x,y = player
	#if move is == to left , x-1
	if move == 'left':
		x -= 1
	elif move == 'right':
		x += 1
	elif move == 'up':
		y -= 1
	elif move == 'down':
		y += 1
	return x,y

def get_moves(player):
	# if players y == 0, they cant move up
	# if players y == GRID_SIZE - 1, they cant move down
	# if players x == 0, cant move left
	# if players y == GRID_SIZE - 1, cant move right
	moves = ['left', 'right', 'up', 'down']
	x, y = player
	if x == 0:
		moves.remove('left')
	elif x == GRID_SIZE - 1:
		moves.remove('right')
	elif y == 0:
		moves.remove('up')
	elif y == GRID_SIZE - 1:
		moves.remove('down')
	return moves

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")




GRID_SIZE = 5
CELLS = create_grid(GRID_SIZE)
monster, door, player = get_locations(CELLS)

while True:
	valid_moves = get_moves(player)
	print("Welcome to the dungeon!")
	print("You're currently in room {}".format(player)) #fill with player position
	print("You can move {}".format(', '.join(valid_moves))) #fill with available moves
	print("Enter 'quit' to exit")

	move = input(">  ").lower()

	if move == 'quit':
		break
	if move in valid_moves:
		player = move_player(player, move)
	else:
		clear_screen()
		print("\n ** Walls are hard! Don't run into them!")
		continue
	clear_screen()

	if player == monster:
		print('you lose!')
		break
	elif player == door:
		print('you win!')
		break
	#good move? change player position
	#bad move? try again dont change anything
	#on door? win!
	#on monster? lose!