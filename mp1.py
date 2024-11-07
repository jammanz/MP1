import sys
import time

# Constants such as the points and the emojis
WALL = "🧱"       
EGG = "🥚"       
GRASS = "🟩"      
NEST_EMPTY = "🪹" 
NEST_WITH_EGGS = "🪺" 
PAN = "🍳" 
NEST_POINT = 10
PAN_POINT = 5


def load_level(): 
    if len(sys.argv) < 2:
        print('The game requires a filename to start.', file=sys.stderr)
        return
    else:
        with open(sys.argv[1], encoding='utf-8') as f:
        	rows_num = int(f.readline().strip())
        	moves_num = int(f.readline().strip())
        	grid = [(f.readline().strip()) for row in range(rows_num)]
            main_game(grid, moves_num)


def main_game():



def tilt():

load_level()

