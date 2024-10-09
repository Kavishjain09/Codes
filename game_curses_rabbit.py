import random
import curses

# Constants for game elements
EMPTY = '-'
RABBIT = 'r'
RABBIT_HOLDING_CARROT = 'R'
CARROT = 'c'
RABBIT_HOLE = 'O'

def generate_map(width, height, num_carrots, num_holes):
    grid = [['-' for _ in range(width)] for _ in range(height)]

    rabbit_x, rabbit_y = random.randint(0, width - 1), random.randint(0, height - 1)
    grid[rabbit_y][rabbit_x] = RABBIT

    for _ in range(num_carrots):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        while grid[y][x] != '-':
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        grid[y][x] = CARROT

    for _ in range(num_holes):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        while grid[y][x] != '-':
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        grid[y][x] = RABBIT_HOLE

    return grid, (rabbit_x, rabbit_y)

def print_grid(win, grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            win.addch(y, x, grid[y][x])

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    height, width = stdscr.getmaxyx()
    num_carrots = 5
    num_holes = 3

    grid, rabbit_position = generate_map(width, height, num_carrots, num_holes)
    carrot_holding = False

    while True:
        stdscr.clear()
        print_grid(stdscr, grid)

        move = stdscr.getch()

        if move == ord('q'):
            break

        x, y = rabbit_position
        new_x, new_y = x, y

        if move == ord('w'):
            new_y -= 1
        elif move == ord('s'):
            new_y += 1
        elif move == ord('a'):
            new_x -= 1
        elif move == ord('d'):
            new_x += 1

        if 0 <= new_x < width and 0 <= new_y < height:
            if grid[new_y][new_x] == CARROT:
                carrot_holding = True
                grid[new_y][new_x] = EMPTY
            elif grid[new_y][new_x] == RABBIT_HOLE and carrot_holding:
                stdscr.addstr(height // 2, width // 2 - 10, "You won! You placed a carrot in a hole.")
                stdscr.refresh()
                stdscr.getch()
                break

            if carrot_holding:
                grid[y][x] = RABBIT_HOLDING_CARROT
            else:
                grid[y][x] = EMPTY

            grid[new_y][new_x] = RABBIT
            rabbit_position = (new_x, new_y)

if __name__ == "__main__":
    curses.wrapper(main)
