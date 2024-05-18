#YukiYan
import random

class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, grid):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] is None:
                grid[self.x][self.y] = None
                grid[new_x][new_y] = self
                self.x, self.y = new_x, new_y
                break

class World:
    def __init__(self, width, height, num_agents):
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.agents = []
        for i in range(num_agents):
            while True:
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)
                if self.grid[x][y] is None:
                    agent = Agent(i, x, y)
                    self.grid[x][y] = agent
                    self.agents.append(agent)
                    break

    def simulate(self):
        for agent in self.agents:
            agent.move(self.grid)

    def display(self):
        for row in self.grid:
            print(' '.join(['A' if cell else '.' for cell in row]))

def main():
    world = World(5, 5, 3)
    print("Initial World:")
    world.display()
    for _ in range(10):  #
        world.simulate()
        print("After move:")
        world.display()

if __name__ == "__main__":
    main()
