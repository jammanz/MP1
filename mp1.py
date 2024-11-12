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
            grid = [f.readline().strip() for row in range(rows_num)]
             
            main_game(grid, moves_num)

                
def main_game(grid, moves_num):
    prev = []
    valid_moves = set(('L', 'l', 'R', 'r', 'F', 'f', 'B', 'b'))
    game_points = 0


    # Test print output
    for row in grid:
        print(row)


    print('Previous Moves:')
    print('Remaining Moves:' + f'{moves_num}')
    print('Points:' + f'{game_points}')
    user_moves = input('Enter Move/s: ')
    print(user_moves)
    # Test print output



    #Valid move check
    if all(move in valid_moves for move in user_moves):
        tilt(grid, user_moves)

    else:
        print('Invalid')
    


def tilt(grid, moves):
    for move in moves:
        if move == 'L' or move == 'l':
            print('test')
        
        if move == 'R' or move == 'R':
            pass
        
        if move == 'F' or move == 'f':
            pass
        
        if move == 'B' or move == 'b':
            pass


load_level()



