import random

# Constants for game elements
EMPTY = '-'
RABBIT = 'r'
RABBIT_HOLDING_CARROT = 'R'
CARROT = 'c'
RABBIT_HOLE = 'O'  
def generate_map(width, height, num_carrots, num_holes):
    # Create an empty grid
    grid = [['-' for _ in range(width)] for _ in range(height)]

    # Place Rabbit
    rabbit_x, rabbit_y = random.randint(0, width - 1), random.randint(0, height - 1)
    grid[rabbit_y][rabbit_x] = RABBIT

    # Place Carrots
    for _ in range(num_carrots):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        while grid[y][x] != '-':
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        grid[y][x] = CARROT

    # Place Rabbit Holes
    for _ in range(num_holes):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        while grid[y][x] != '-':
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        grid[y][x] = RABBIT_HOLE

    return grid, (rabbit_x, rabbit_y)

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def main():

    width = int(input("Enter the width of the game grid: "))
    height = int(input("Enter the height of the game grid: "))
    num_carrots = int(input("Enter the number of carrots: "))
    num_holes = int(input("Enter the number of rabbit holes: "))

    grid, rabbit_position = generate_map(width, height, num_carrots, num_holes)
    carrot_holding = False

    while True:
        print_grid(grid)

        move = input("\n(Press 'w'/'a'/'s'/'d' for Directions\n'p' for Pick the Carrot or Place the Carrot into the Hole\nPress 'j' for Jump\nPress 'q' for Exit)\nEnter your move: ").lower()

        if move == 'q':
            print("Goodbye!")
            break

        x, y = rabbit_position
        new_x, new_y = x, y
        # Set directions to move rabbit
        if move == 'w' and grid[new_y-1][new_x] != 'O' and grid[new_y-1][new_x] != 'c':
            new_y -= 1
        elif move == 's' and grid[new_y+1][new_x] != 'O' and grid[new_y+1][new_x] != 'c':
            new_y += 1
        elif move == 'a' and grid[new_y][new_x-1] != 'O' and grid[new_y][new_x-1] != 'c':
            new_x -= 1
        elif move == 'd' and grid[new_y][new_x+1] != 'O'  and grid[new_y][new_x+1] != 'c':
            new_x += 1
        elif move == 'j':
        # Check if there's a hole on the left
            if new_x > 0 and grid[new_y][new_x-1] == 'O':
                new_x -= 2
        # Check if there's a hole above
            elif new_y > 0 and grid[new_y-1][new_x] == 'O':
                new_y -= 2
        # Check if there's a hole to the right
            elif new_x < len(grid[0]) - 1 and grid[new_y][new_x+1] == 'O':
                new_x += 2
        # Check if there's a hole below
            elif new_y < len(grid) - 1 and grid[new_y+1][new_x] == 'O':
                new_y += 2
        elif move== 'p':
            # Check if there's a carrot on the left
            if new_x > 0 and grid[new_y][new_x-1] == 'c' and carrot_holding==False:
                grid[new_y][new_x-1]=EMPTY
                carrot_holding=True
        # Check if there's a carrot above
            elif new_y > 0 and grid[new_y-1][new_x] == 'c' and carrot_holding==False:
                grid[new_y-1][new_x]=EMPTY
                carrot_holding=True
        # Check if there's a carrot to the right
            elif new_x < len(grid[0]) - 1 and grid[new_y][new_x+1] == 'c' and carrot_holding==False:
                grid[new_y][new_x+1]=EMPTY
                carrot_holding=True
        # Check if there's a carrot below
            elif new_y < len(grid) - 1 and grid[new_y+1][new_x] == 'c' and carrot_holding==False:
                grid[new_y+1][new_x]=EMPTY
                carrot_holding=True
                   # Check if there's a hole on the left
            elif new_x > 0 and grid[new_y][new_x-1] == 'O' and carrot_holding:
                print("You won! You placed a carrot in a hole.")
                break
        # Check if there's a hole above
            elif new_y > 0 and grid[new_y-1][new_x] == 'O' and carrot_holding:
                print("You won! You placed a carrot in a hole.")
                break
        # Check if there's a hole to the right
            elif new_x < len(grid[0]) - 1 and grid[new_y][new_x+1] == 'O' and carrot_holding:
                print("You won! You placed a carrot in a hole.")
                break
        # Check if there's a hole below
            elif new_y < len(grid) - 1 and grid[new_y+1][new_x] == 'O' and carrot_holding:
                print("You won! You placed a carrot in a hole.")
                break

        if carrot_holding:
            grid[new_y][new_x] = RABBIT_HOLDING_CARROT
            grid[y][x]=EMPTY
        else:
            grid[y][x] = EMPTY
            
        grid[new_y][new_x] = RABBIT
        if carrot_holding:
            grid[new_y][new_x] = RABBIT_HOLDING_CARROT
        rabbit_position = (new_x, new_y)

if __name__ == "__main__":
    main()