import npyscreen
import random

# Constants for game elements
EMPTY = '-'
PLAYER = 'P'
ITEM = 'C'
OBSTACLE = 'X'

class GameForm(npyscreen.FormBaseNew):

    def create(self):
        self.player_position = [0, 0]
        self.grid_size = [20, 20]
        self.items = [(random.randint(0, self.grid_size[0]-1), random.randint(0, self.grid_size[1]-1)) for _ in range(10)]
        self.obstacles = [(random.randint(0, self.grid_size[0]-1), random.randint(0, self.grid_size[1]-1)) for _ in range(10)]
        self.game_over = False

    def draw_grid(self):
        grid = [[EMPTY for _ in range(self.grid_size[0])] for _ in range(self.grid_size[1])]
        x, y = self.player_position
        grid[y][x] = PLAYER

        for item in self.items:
            x, y = item
            grid[y][x] = ITEM

        for obstacle in self.obstacles:
            x, y = obstacle
            grid[y][x] = OBSTACLE

        return grid

    def on_timer(self):
        if not self.game_over:
            self.move_player()

    def move_player(self):
        x, y = self.player_position
        direction = self.get_input()
        new_x, new_y = x, y

        if direction == 'w':
            new_y -= 1
        elif direction == 's':
            new_y += 1
        elif direction == 'a':
            new_x -= 1
        elif direction == 'd':
            new_x += 1

        if 0 <= new_x < self.grid_size[0] and 0 <= new_y < self.grid_size[1]:
            if (new_x, new_y) in self.items:
                self.items.remove((new_x, new_y))
            elif (new_x, new_y) in self.obstacles:
                self.game_over = True
                return

            self.player_position = [new_x, new_y]
            self.display()

    def get_input(self):
        key = self.getch()
        if key == ord('q'):
            self.parentApp.switchForm(None)
        elif key == ord('w'):
            return 'w'
        elif key == ord('s'):
            return 's'
        elif key == ord('a'):
            return 'a'
        elif key == ord('d'):
            return 'd'
        return None

    def while_waiting(self):
        self.move_player()
        self.display()

class GameApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", GameForm)

if __name__ == "__main__":
    app = GameApp().run()
