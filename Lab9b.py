#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:09:53 2024

@author: yifeisu
"""

import random


class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, grid):
     
        options = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] is None]
        if options:
            new_position = random.choice(options)
            grid[self.x][self.y], grid[new_position[0]][new_position[1]] = None, self

            self.x, self.y = new_position

class World:
    def __init__(self, grid_size, num_agents):
        self.grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        self.agents = []
        for i in range(num_agents):
            while True:
                x, y = random.randint(0, grid_size-1), random.randint(0, grid_size-1)
                if self.grid[x][y] is None:
                    self.grid[x][y] = Agent(i, x, y)
                    self.agents.append(self.grid[x][y])
                    break

    def simulate(self, moves):
        for _ in range(moves):
            random.shuffle(self.agents)
            for agent in self.agents:
                agent.move(self.grid)


grid_size = 10 
num_agents = 20 
moves = 50 


world = World(grid_size, num_agents)
world.simulate(moves)

#repo:https://github.com/yifeis0810/Week-9-lab