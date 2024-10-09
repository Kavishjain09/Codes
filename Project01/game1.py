import random

# Function to generate a random map
def generate_map(size, num_carrots, num_holes):
    # Initialize an empty grid
    grid = [['-' for _ in range(size)] for _ in range(size)]
    
    # Place rabbit randomly
    rabbit_x, rabbit_y = random.randint(0, size-1), random.randint(0, size-1)
    grid[rabbit_x][rabbit_y] = 'r'
    
    # Place carrots randomly
    for _ in range(num_carrots):
        while True:
            x, y = random.randint(0, size-1), random.randint(0, size-1)
            if grid[x][y] == '-':
                grid[x][y] = 'c'
                break
    # Place rabbit holes randomly
    for _ in range(num_holes):
        while True:
            x, y = random.randint(0, size-1), random.randint(0, size-1)
            if grid[x][y] == '-':
                grid[x][y] = 'O'
                break
    return grid

# Function to display the map
def display_map(grid):
    for row in grid:
        print(' '.join(row))

# Function to move the rabbit
def move_rabbit(grid, direction):
    rabbit_x, rabbit_y = -1, -1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'r' or grid[i][j] == 'R':
                rabbit_x, rabbit_y = i, j
    
    if direction == 'a':  # Move left
        if rabbit_y > 0 and grid[rabbit_x][rabbit_y-1] != 'c':
            grid[rabbit_x][rabbit_y], grid[rabbit_x][rabbit_y-1] = grid[rabbit_x][rabbit_y-1], grid[rabbit_x][rabbit_y]
    elif direction == 'd':  # Move right
        if rabbit_y < len(grid[0]) - 1 and grid[rabbit_x][rabbit_y+1] != 'c':
            grid[rabbit_x][rabbit_y], grid[rabbit_x][rabbit_y+1] = grid[rabbit_x][rabbit_y+1], grid[rabbit_x][rabbit_y]
    elif direction == 'w':  # Move up
        if rabbit_x > 0 and grid[rabbit_x-1][rabbit_y] != 'c':
            grid[rabbit_x][rabbit_y], grid[rabbit_x-1][rabbit_y] = grid[rabbit_x-1][rabbit_y], grid[rabbit_x][rabbit_y]
    elif direction == 's':  # Move down
        if rabbit_x < len(grid) - 1 and grid[rabbit_x+1][rabbit_y] != 'c':
            grid[rabbit_x][rabbit_y], grid[rabbit_x+1][rabbit_y] = grid[rabbit_x+1][rabbit_y], grid[rabbit_x][rabbit_y]
# Function to pick up carrots
def pick_up_carrot(grid):
    rabbit_x, rabbit_y = -1, -1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'r':
                rabbit_x, rabbit_y = i, j
    # Rabbit holds a carrot
    if rabbit_y > 0 and grid[rabbit_x][rabbit_y-1] =='c':
        grid[rabbit_x][rabbit_y-1] = 'R'
        grid[rabbit_x][rabbit_y] == '-'
        grid[rabbit_x][rabbit_y], grid[rabbit_x][rabbit_y-1] = grid[rabbit_x][rabbit_y-1], grid[rabbit_x][rabbit_y]

    elif rabbit_y < len(grid[0]) - 1 and grid[rabbit_x][rabbit_y+1] != 'c':
            grid[rabbit_x][rabbit_y] == '-'
            grid[rabbit_x][rabbit_y+1] = 'R'
            grid[rabbit_x][rabbit_y], grid[rabbit_x][rabbit_y+1] = grid[rabbit_x][rabbit_y+1], grid[rabbit_x][rabbit_y]

    elif rabbit_x > 0 and grid[rabbit_x-1][rabbit_y] != 'c':
            grid[rabbit_x][rabbit_y] == '-'
            grid[rabbit_x-1][rabbit_y] = 'R'
            grid[rabbit_x][rabbit_y], grid[rabbit_x-1][rabbit_y] = grid[rabbit_x-1][rabbit_y], grid[rabbit_x][rabbit_y]
 
    elif rabbit_x < len(grid) - 1 and grid[rabbit_x+1][rabbit_y] != 'c':
            grid[rabbit_x][rabbit_y] == '-'
            grid[rabbit_x+1][rabbit_y] = 'R'   
            grid[rabbit_x][rabbit_y], grid[rabbit_x+1][rabbit_y] = grid[rabbit_x+1][rabbit_y], grid[rabbit_x][rabbit_y]
          
    
    
# Rabbit holds a carrot

# Function to jump rabbit holes
def jump_hole(grid):
    rabbit_x, rabbit_y = -1, -1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'r':
                rabbit_x, rabbit_y = i, j
    
    if grid[rabbit_x][rabbit_y] == 'O':
        # Check if there's a hole on the left
        if rabbit_y > 0 and grid[rabbit_x][rabbit_y-1] == 'O':
            grid[rabbit_x][rabbit_y], grid[rabbit_x][rabbit_y-1] = grid[rabbit_x][rabbit_y-1], grid[rabbit_x][rabbit_y]
        # Check if there's a hole above
        elif rabbit_x > 0 and grid[rabbit_x-1][rabbit_y] == 'O':
            grid[rabbit_x][rabbit_y], grid[rabbit_x-1][rabbit_y] = grid[rabbit_x-1][rabbit_y], grid[rabbit_x][rabbit_y]
        # Check if there's a hole to the right
        elif rabbit_y < len(grid[0]) - 1 and grid[rabbit_x][rabbit_y+1] == 'O':
            grid[rabbit_x][rabbit_y], grid[rabbit_x][rabbit_y+1] = grid[rabbit_x][rabbit_y+1], grid[rabbit_x][rabbit_y]
        # Check if there's a hole below
        elif rabbit_x < len(grid) - 1 and grid[rabbit_x+1][rabbit_y] == 'O':
            grid[rabbit_x][rabbit_y], grid[rabbit_x+1][rabbit_y] = grid[rabbit_x+1][rabbit_y], grid[rabbit_x][rabbit_y]

# Function to place a carrot into a hole
def place_carrot_in_hole(grid):
    rabbit_x, rabbit_y = -1, -1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'R':
                rabbit_x, rabbit_y = i, j
    
    # Check if there's a hole on the left
    if rabbit_y > 0 and grid[rabbit_x][rabbit_y-1] == 'O':
        grid[rabbit_x][rabbit_y-1] = 'C'  # Carrot placed in hole
        grid[rabbit_x][rabbit_y] = '-'  # Rabbit loses the carrot
    # Check if there's a hole above
    elif rabbit_x > 0 and grid[rabbit_x-1][rabbit_y] == 'O':
        grid[rabbit_x-1][rabbit_y] = 'C'
        grid[rabbit_x][rabbit_y] = '-'
    # Check if there's a hole to the right
    elif rabbit_y < len(grid[0]) - 1 and grid[rabbit_x][rabbit_y+1] == 'O':
        grid[rabbit_x][rabbit_y+1] = 'C'
        grid[rabbit_x][rabbit_y] = '-'
    # Check if there's a hole below
    elif rabbit_x < len(grid) - 1 and grid[rabbit_x+1][rabbit_y] == 'O':
        grid[rabbit_x+1][rabbit_y] = 'C'
        grid[rabbit_x][rabbit_y] = '-'

# Main game loop
if __name__ == "__main__":
    while True:
        try:
            size = int(input("Enter grid size: "))
            num_carrots = int(input("Enter number of carrots: "))
            num_holes = int(input("Enter number of holes: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    game_map = generate_map(size, num_carrots, num_holes)
    
    while True:
        display_map(game_map)
        move = input("Enter your move (a: left, d: right, w: up, s: down, p: pick carrot, j: jump hole, q: quit): ")
        
        if move == 'q':
            break
        elif move in ('a', 'd', 'w', 's'):
            move_rabbit(game_map, move)
        elif move == 'p':
            pick_up_carrot(game_map)
        elif move == 'j':
            jump_hole(game_map)
        elif move == 'p':
            place_carrot_in_hole(game_map)
        # Check for win condition
        if 'c' not in ''.join([''.join(row) for row in game_map]):
            display_map(game_map)
            print("Congratulations! You've deposited a carrot into a hole.")
            break
    print("Game over.")
